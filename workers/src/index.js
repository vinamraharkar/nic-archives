const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
  });
}

async function embedQuery(query, env) {
  const resp = await fetch("https://api.jina.ai/v1/embeddings", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${env.JINA_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "jina-embeddings-v3",
      task: "retrieval.query",
      dimensions: 1024,
      input: [query],
    }),
  });
  if (!resp.ok) throw new Error(`Jina embed error: ${resp.status}`);
  const data = await resp.json();
  return data.data[0].embedding;
}

function queryTokens(query) {
  return new Set(query.toLowerCase().split(/[\s\-_.,;:!?()]+/).filter((t) => t.length > 3));
}

function tokenOverlap(qTokens, text) {
  if (!text || qTokens.size === 0) return 0;
  const words = text.toLowerCase().split(/[\s\-_.,;:!?()]+/).filter((t) => t.length > 3);
  const matches = words.filter((w) => qTokens.has(w)).length;
  return matches / qTokens.size;
}

async function search(query, limit, env) {
  const queryVec = await embedQuery(query, env);
  const qTokens = queryTokens(query);

  // Vectorize ANN query — topK=20 to get enough chunks to de-dupe into top-10 articles
  const vectorResult = await env.VECTORIZE.query(queryVec, {
    topK: 20,
    returnMetadata: "all",
    returnValues: false,
  });

  // De-dupe chunks by article slug, keeping highest-score chunk per article
  const bySlug = new Map();
  for (const match of vectorResult.matches) {
    const { slug, title, issue_date, url, body_snippet } = match.metadata;
    const existing = bySlug.get(slug);
    if (!existing || match.score > existing.score) {
      bySlug.set(slug, { slug, title, issue_date, url, body_snippet, score: match.score });
    }
  }

  // Token-overlap boost: reward articles whose title/slug share query terms
  const articles = [...bySlug.values()];
  for (const article of articles) {
    const titleBoost = 0.10 * tokenOverlap(qTokens, article.title);
    const slugBoost = 0.05 * tokenOverlap(qTokens, article.slug.replace(/-/g, " "));
    article.score += titleBoost + slugBoost;
  }

  articles.sort((a, b) => b.score - a.score);
  return articles.slice(0, limit);
}

async function ask(query, env) {
  const topResults = await search(query, 5, env);

  if (topResults.length === 0) {
    return { answer: "No relevant articles found.", citations: [] };
  }

  const context = topResults
    .map((r, i) => `[${i + 1}] "${r.title}" (${r.issue_date})\n${r.body_snippet}`)
    .join("\n\n");

  const systemPrompt =
    "You are an expert on NIC (National Informatics Centre) India's history and e-governance work. " +
    "Answer questions using ONLY the provided sources. " +
    "Always summarise the answer in 2-3 lines — give the user the core insight, not an exhaustive list. Do not use bullet points or lists. " +
    "If sources don't contain enough information, say so in one sentence.";

  const userPrompt = `Sources:\n${context}\n\nQuestion: ${query}\n\nAnswer:`;

  const geminiResp = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${env.GEMINI_API_KEY}`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        systemInstruction: { parts: [{ text: systemPrompt }] },
        contents: [{ parts: [{ text: userPrompt }] }],
        generationConfig: {
          maxOutputTokens: 2048,
          thinkingConfig: { thinkingBudget: 0 },
        },
      }),
    }
  );

  if (!geminiResp.ok) {
    throw new Error(`Gemini API error: ${geminiResp.status}`);
  }

  const geminiData = await geminiResp.json();
  const answer = geminiData?.candidates?.[0]?.content?.parts?.[0]?.text ?? "Could not generate answer.";

  return {
    answer,
    citations: topResults.map(({ slug, title, issue_date, url }) => ({ slug, title, issue_date, url })),
  };
}

export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: CORS_HEADERS });
    }

    const url = new URL(request.url);

    if (request.method !== "POST") {
      return json({ error: "Method not allowed" }, 405);
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return json({ error: "Invalid JSON" }, 400);
    }

    if (url.pathname === "/search") {
      if (!body.query) return json({ error: "query required" }, 400);
      const limit = Math.min(body.limit ?? 10, 50);
      try {
        const results = await search(body.query, limit, env);
        return json(results);
      } catch (e) {
        return json({ error: "Search failed: " + e.message }, 500);
      }
    }

    if (url.pathname === "/ask") {
      if (!body.query) return json({ error: "query required" }, 400);
      try {
        const result = await ask(body.query, env);
        return json(result);
      } catch (e) {
        return json({ error: "Ask failed: " + e.message }, 500);
      }
    }

    return json({ error: "Not found" }, 404);
  },
};
