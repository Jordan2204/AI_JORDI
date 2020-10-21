class Time():
    """
        Cette classe permet de donner des infos sur le temps 
    
    """
    def __init__(self, datetime, speak):
        self.datetime = datetime
        self.speak = speak.speak  
    
    def time(self):
        """ Recuperation de l'heure et lecture par l'IA """
        Time = self.datetime.datetime.now().strftime("%H:%M:%S")
        self.speak("The current time is")
        self.speak(Time)
    
    def date(self):
        year = int(self.datetime.datetime.now().year)
        month = int(self.datetime.datetime.now().month)
        day = int(self.datetime.datetime.now().day)
        self.speak(" Nous somme le ")
    
        self.speak(day)
        self.speak(month)
        self.speak(year) 
    
    def salutation(self):
        hour = int(self.datetime.datetime.now().hour)
        if( hour >= 6 and hour < 12):
            self.speak("Bienvenue et bonjour Monsieur Jordane")
        elif (hour >= 12 and (hour < 18)):
            self.speak("Bienvenue et Bonne apres midi Monsieur Jordane")
        elif (hour >= 16 and hour < 24):
            self.speak(" Bienvenur et Bonsoir Monsieur Jordane")
        else:
            self.speak("Bonne nuit Monsieur ")   
    
    def wishme(self):
        """ Fonction pour une phrase de bienvenue """
        self.speak("Je suis a votre service dites- moi ce que je peux faire pour vous !")
