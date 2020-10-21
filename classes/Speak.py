class Speak():
    """
        Cette classe permet de transformer le texte en voix
    
    """
    def __init__(self,engine):
        self.engine = engine
    
    def speak(self,audio):
        """ Fonction qui prend un texte en parametre et le lit """
        
        self.engine.say(audio)
        self.engine.runAndWait()