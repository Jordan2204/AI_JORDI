class Translation(object):
    """ 
        Cette classe permettra de gérer le multi langue francais et anglais
        y compris l'utilisation des expressions régulière. fr = 0, en = 1
    """
    def __init__(self,lang=0):
        super().__init__()
        
        self.lang = lang
    
    def setCurLang(self,lang):
        self.lang = lang
        
    def getCurLang(self,lang):
        return self.lang
    
    def changLang(self):
        chlang = ["changer de langue", "Change the langage"]
        return chlang[self.lang]

    def salutation(self):
        saluer = {
            "jour" : ["Bienvenue et bonjour Monsieur Jordane","Welcome an good morning sir Jordan"],
            "apresm" : ["Bienvenue et Bonne apres midi Monsieur Jordane"," Welcome an good afternoon sir Jordan"],
            "soir" : ["Bienvenu et Bonsoir Monsieur Jordane","Welcome an good evening sir Jordan"],
            "nuit" : ["Bonne nuit Monsieur ","good night sir Jordan"]
            }    
        return saluer
    
    def wishme(self):
        wish = ["Je suis a votre service dites-moi ce que je peux faire pour vous !","I am at your service tel me what can i do !"]
        return wish[self.lang]
    
    def time(self):
        time = ["Il est ","The current time is"]    
        return time[self.lang]
    
    def date(self):
        date = ["Nous sommes le  ", "We are the "]
        return date[self.lang]
    
    def wikipedia(self):
        wiki = ["wikipédia", "wikipedia"]
        return wiki[self.lang]
    
    def textSearch(self):
        search = ["Recherche", "Searching"]
        return search[self.lang]
    
    def noResult(self):
        nrs = ["aucun resultat !"," no result sir !"]
    
    #Pour les mails
    def whatSayMail(self):
        whatsSay = ["ques-ce que je dois dire ?"," What can i say ?"]
        return whatsSay[self.lang]
    
    def toWho(self):
        towho = ["a qui ?"," To who ?"] 
        return towho[self.lang]
    
    def mailSend(self):
        ms = ["l'email a été envoyer !"," the email has been send"]
        return ms[self.lang]
    
    def errormail(self):
        err = ["impossible d'envoyer l'email"," i can't send email"]
        
        return err[self.lang]
    
    #Pour les navigateurs
    def searchIn(self):
        search = ["recherche dans chrome"," search in chrome"]
        return search[self.lang]
    
    def whatSearch(self):
        whats = ["Ques-ce que je dois chercher Mr ?", " What can i search sir ?"]
        return whats[self.lang]
    
    #Sauvegarde de message
    def remember(self):
        rmber = ["souviens-toi de"," Remember that "]
        return rmber[self.lang]
    
    def whatrmber(self):
        whatrmber = ["De quoi devrais-je me souvenir ?"," What can i remember"]
        return whatrmber[self.lang]
    
    def irmber(self):
        irmber = ["vous m'avez demander de me souvenir de la phrase :"," you tel me to remember that "]
        return irmber[self.lang]
    
    def iknow(self):
        ikwn = ["connais-tu quelque chose ?"," do you know anything ?"]
        return ikwn[self.lang]
    
    def ytellme(self):
        ytllme = ["vous m'avez demander de me souvenir de"," you told me to remember that"]
        return ytllme[self.lang]
    
    #Les taches systemes
    def cpu(self):
        pross = ["cpu", "cpu"]
        return pross[self.lang]
    
    def blague(self):
        blg = ["une blague", "joke"]
        return blg[self.lang]
    
    def screenshut(self):
        sc = ["screenshot", "screenshot"]
        return sc[self.lang]
    
    def shutdwn(self):
        sh = ["éteint l'ordi", " shutdown computer"]
        return sh[self.lang]
    
    def taskEnd(self):
        taskend = ["Terminer","Finish"]
        return taskend[self.lang]
    
    def msgshdw(self):
        msgsht = ["Je vais éteindre l'ordinateur dans 600 secondes", "a will shutdown the computer in 600 seconds"]
        return msgsht[self.lang]  
    
    def noshut(self):
        nosht = ["annule l'arrêt"," don't shut computer"]
        return nosht[self.lang] 
    
    def msgshtend(self):
        msgshutend = ["l'extinction a été annuler Mr."," The shutdown has been canceled"]
        return msgshutend[self.lang]
    
    def rboot(self):
        rbt = ["redémarre le systeme", " reboot system"]
        return rbt[self.lang]
    
    def msgrbt(self):
        msgrbt = ["Le systeme sera redemarrer dans 600 secondes", "the system will reboot in 600 second"]
        return msgrbt[self.lang]
    
    def creator(self):
        creatr = ["ton créateur"," who create you ?"]
        return creatr[self.lang]
    
    def stoplisten(self):
        stplistn = ["arrête d'écouter"," stop listen"]
        return [self.lang]
    
    def okstoplisten(self):
        okstplisten = ["d'accord Mr "," ok sir"]
        return [okstplisten[self.lang]]
    
    def repos(self):
        rpos = ["repose-toi"," go sleep"]
        return rpos[self.lang]
    
    def goodbye(self):
        goodby = ["Aurevoir Patron."," bye Sir"]
        return goodby[self.lang]
    
