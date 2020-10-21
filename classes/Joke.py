class Joke(object):
    """ Classe qui permet de generer des blagues et citations """
    def __init__(self, pyjokes, speak):
        self.pyjokes = pyjokes
        self.speak = speak.speak
        
    def jokes(self):
        self.speak(self.pyjokes.get_joke())
        