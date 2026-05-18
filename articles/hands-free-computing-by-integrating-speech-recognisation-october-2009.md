---
title: "Hands Free Computing by Integrating Speech Recognisation"
publication: "Informatics"
issue_date: "October 2009"
pages: [30, 31]
author: "Niladri Bihari Mohanty, Ravindra Kumar Jaiswal"
section: "Technology Update"
---

## Hands Free Computing by Integrating Speech Recognisation

Voice reorganization and text to speech system is becoming a powerful tool to provide the services through ICT for the physically handicapped people. While entering to ATM counters and just after swapping the ATM card in the reader, a greeting voice as well as guiding instruction can be heard in almost all ATM counters, which is of course a commendable step to bring those physically handicapped people to the domain of ATM user. As it is just an innovative thought to use the technological power of Speech synthesis into a way to increase quality of service in the Banking sector, so in the same way e-Governance services can become more reachable by the use of this technology in an innovative way.
Government of India and State Governments are providing various kind of facilitation for the betterment of physically challenged persons by providing them education and employment, so e-Governance application should also target this section of the user by providing additional functionalities for them. Integration of Voice Recognition system in e-Governance and making them language interoperable can address the challenges of this section as well as a great solution for those who haven't came out from illiteracy to e-Literacy as they don't need to use any electronic gadgets. Developing voice enable software application is not at all a rocket science technology. In this article it has been outlined, some of the basic tricks to Integrate Speech Recognition and Text to Speech feature for Microsoft .net Framework coded in both VB.net as well as C#.net.
Speech API consists of two types of services. First one is converting text to speech using configured synthesized voice and second is speech Recognition in Dictation mode as well as in command mode. In the quick start we may follow examples as bellow.
Example for Text-to-Speech conversion
Step1. Create a New project using VB.net or C#.net
— Add a TextBox named txt_speek and a Button name btn_sub
Step2. Add Reference. Procedure is same for both VB and C# languages. In the solution Explorer Right Click on the root element and choose Add Reference.
— In the COM tab select sample TTS engine and holding the 'Ctrl' key select Microsoft Speech Object Library
Step3. Imports the Speech Library
In VB: Imports speechLib
In C#: Using speechLib
Step4. Call the speak Method of spVoice object in the Button click event.
In VB:
Dim Voice As SpVoice = New SpVoice()
Voice.Speak(text,SpeechVoiceSpeakFlags.SVSFDefault)
In C#:
SpVoice voice= New SpVoice();
Voice.Speak(text,SpeechVoiceSpeakFlags.SVSFDefault);
Now your programme is ready to speak what ever you write in the text box. There are lot of features in the API to adjust volume, rate of Speech, Pitch, Voice and many more which can be explored by little trial and error method by the interested reader.
Example for Speech Recognition
Step1.
— Create a New project usingVB.net or C#.net
— Add a TextBox named txt_rec
Step2. Add Reference. Procedure is same for both VB and C# languages.
— In the solution Explorer Right Click on the root element and choose Add Reference.
— In the COM tab select sample TTS engine and holding the 'Ctrl' key select Microsoft Speech Object Library
Step3. Imports the Speech Library
In VB: Imports speechLib
In C#: Using speechLib
Step4. Create the Event
In VB:
public sub RecoContext_Recognition (Byval StreamNumber as Integer,Byval StreamPosition as Object, Byval RecognitionType as Speech Recognition Type, Byval Result as ISpeech RecoResult)
//Get the text from the speech //received from Microphone
dim word as string = Result.PhraseInfo.GetText(0, -1, true)
textBox1.AppendText(word)
End Sub
In C#:
public void Reco Context_Recognition (int Stream Number, object Stream Position, SpeechRecognitionType Recognition Type, I Speech Reco Result Result)
{
//Get the text from the text //received from Microphone
string word = Result.PhraseInfo.GetText(0, -1, true);
txt_rec.AppendText(word);
}
Step5. Register the event in Form Load
In VB:
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
Dim objRecoContext As New SpSharedRecoContext
AddHandler objRecoContext.Recognition, AddressOf RecoContext_Recognition
Dim grammar As ISpeechRecoGrammar = objRecoContext.CreateGrammar(0)
grammar.DictationSetState(SpeechRuleState.SGDSActive)
End Sub
In C#:
private void Form1_Load(object sender, EventArgs e)
{
SpSharedRecoContext objRecoContext = new SpSharedRecoContext();
objRecoContext.Recognition += new _ISpeechRecoContextEvents_RecognitionEventHandler(RecoContext_Recognition);
ISpeechRecoGrammar grammar = objRecoContext.CreateGrammar(0);
grammar.DictationSetState(SpeechRuleState.SGDSActive);}
Now the Application is ready to receive voice from the Microphone and convert that to Text to display in the text box. The speech engine provided by Microsoft i.e Microsoft Speech SDK although is a powerful tool for integrating speech Recognition but have certain major challenges. It is not so much efficient to work with Indian language and Indian accent. Many Other speech engines are available which support Indian accent. Among which 'Bhasana' developed by CDAC Department of IT, Govt of India may be the most suitable. It has three Databases as 'Bhavna' (Emotion Database), 'Uchharak' (Language Database), 'Anuvaachak' (Accent Database). I hope this article will give an initial boost for the developer.
