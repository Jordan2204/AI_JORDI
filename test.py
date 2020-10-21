import pyttsx3  #pip  install pyttsx3 package test to speach pour traduire le texte en parole
import datetime
import speech_recognition as sr

engine = pyttsx3.init()

#Type de voix
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print(voices)
#Vitesse de lecture
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 60)

#Volume
volume = engine.getProperty('volume')
engine.setProperty('volume', 0.95)
   
#Fonction qui prend un texte en parametre et le lis
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
       
        audio = r.listen(source)
        try:
            print("Recognizning...")
            query = r.recognize_google(audio,language='en-in') #fr ou en-in
            print(query)
        except Exception as e:
            print(e)
            speak("Say That again please...")
            return "None"
        
        return query

speak("Je suis un programme d'IA encore en développement")
speak('I am a IA program in development')
takeComand()