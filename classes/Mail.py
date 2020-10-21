class Mail():
    """ Envoi des mail par commande vocale """
    def __init__(self,smtplib):
        self.smtplib  = smtplib

        
    def sendEmail(self, to,content):
        server = self.smtplib.SMTP("smtp.gmail",587)
        server.ehlo()
        server.starttls()
        server.login("anafackjordan@gmail.com","AccountGoogleJordi@@##")
        server.sendmail("anafackjordan@gmail.com",to,content)
