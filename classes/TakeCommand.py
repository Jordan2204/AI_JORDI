class TakeCommand(object):
    """ Cette classe permet de recuperer les commmandes vocales """
    
    def __init__(self, sr, speak):
        self.speech_recognition = sr
        self.speak = speak.speak
        
    def takeComand(self):
        r = self.speech_recognition.Recognizer()
        with self.speech_recognition.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

            try:
                print("Recognizning...")
                query = r.recognize_google(audio,language='fr') #fr ou en-in
                print(query)
            except Exception as e:
                print(e)
                self.speak("Veuillez repeté sil vous plait...")
                return "None"
            
            return query