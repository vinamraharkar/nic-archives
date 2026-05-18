---
title: "DeepSeek-R1: China’s Open-Source Leap in AI Reasoning"
publication: "Informatics"
issue_date: "January 2025"
pages: [41]
author: null
section: "International eGov Update"
---

## DeepSeek-R1: China’s Open-Source Leap in AI Reasoning

The global AI landscape is witnessing a significant shift as open-source models continue to challenge proprietary giants. DeepSeek, a Chinese AI startup renowned for its commitment to open technologies, has unveiled DeepSeek-R1, an advanced reasoning model that rivals OpenAI’s o1 in mathematics, coding, and logical reasoning. The highlight? It delivers comparable performance at a fraction of the cost.
Built on the DeepSeek V3 mixture-of-experts model, DeepSeek-R1 advances the open-source movement by narrowing the performance gap between publicly available models and proprietary solutions. Notably, the model has been instrumental in distilling six Llama and Qwen models, enhancing their capabilities. In some benchmarks, a distilled Qwen-1.5B model outperformed GPT-4o and Claude 3.5 Sonnet in select mathematical tasks, proving the potential of open-source AI.
All these models, including DeepSeek-R1, are open-source and accessible on Hugging Face under an MIT license, reinforcing the drive towards AI democratization.
DeepSeek-R1 exhibits performance on par with OpenAI’s o1, demonstrating its strength in logical reasoning and problem-solving:
• Mathematics: Scored 79.8% on AIME 2024 (vs. o1’s 79.2%) and 97.3% on MATH-500 (vs. o1’s 96.4%).
• Coding: Achieved a Codeforces rating of 2,029, outperforming 96.3% of human programmers.
• General Knowledge: Attained 90.8% accuracy on MMLU, closely trailing o1’s 91.8%.
These numbers demonstrate that open-source models are rapidly closing the gap with proprietary solutions, providing scalable and cost-effective alternatives.
DeepSeek-R1’s development followed a multi-stage training approach, combining reinforcement learning (RL) and supervised fine-tuning:
• RL-Driven Self-Evolution (DeepSeek-R1-Zero): The initial model was trained entirely using trial-and-error reinforcement learning, leading to significant reasoning advancements but also challenges in readability and consistency.
• Refinement Through Supervised Learning: Addressing these issues, DeepSeek incorporated supervised fine-tuning on curated datasets, improving fluency, coherence, and factual accuracy.
• Final Optimization: The model underwent an additional RL phase, fine-tuning responses across mathematics, logical reasoning, factual QA, and cognitive tasks.
This hybrid approach enabled DeepSeek-R1 to achieve performance parity with OpenAI’s o1-1217 while maintaining language precision and logical consistency.
A major differentiator for DeepSeek-R1 is its affordability. Compared to OpenAI’s premium-priced o1, DeepSeek-R1 offers a 90-95% cost reduction:
Model Input Token Cost (per million) Output Token Cost (per million)
OpenAI o1 $15.00 $60.00
DeepSeek-R1 $0.55 $2.19
This drastic price advantage makes DeepSeek-R1 a compelling choice for enterprises, developers, and AI researchers seeking high-performance reasoning models at a sustainable cost.
DeepSeek has made its model widely accessible:
• Test as “DeepThink” on DeepSeek’s chat platform (akin to ChatGPT).
• Download the model weights & code from Hugging Face (MIT license).
• Use the API for seamless integration into applications.
DeepSeek’s move strengthens the open-source AI movement, proving that publicly available models can rival closed commercial solutions. With the continued push toward Artificial General Intelligence (AGI), advancements like DeepSeek-R1 demonstrate that the future of AI is not just exclusive to tech giants—but a collaborative and accessible endeavor.
By prioritizing affordability, transparency, and high performance, DeepSeek is reshaping the AI landscape, proving that open-source models are no longer just alternatives—they are contenders. The race for AI dominance is now an open battlefield.
