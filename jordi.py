import pyttsx3 #pip  install pyttsx3 package text to speach pour traduire le texte en parole
import datetime
import speech_recognition as sr #pip install SpeechRecognition pour les commandes vocales 
import smtplib #Pour la messagerie
import os #Pour les commandes system
import pyautogui #pip install pyautogui
import random
import psutil #pip install psutil : pour le cpu, batterie
import pyjokes
import wikipedia #pip install wikipedia : pour fournir a notre IA des ressources de wikipedia
import webbrowser as wb #Pour la gestion du navigateur

#Importation des configs
from globalVar import *

from classes.Speak import *
from classes.Time import *
from classes.TakeCommand import *
from classes.System import *
from classes.Joke import *
from classes.Mail import *
from functions import *
from classes.Translation import *
#Configuration du package de traduction
engine = pyttsx3.init()

#Types de voix
try:
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
except Exception as e:
    print(e)

#Vitesse de lecture
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 40)

#Volume
volume = engine.getProperty('volume')
engine.setProperty('volume', 0.90)
   
#Instanciation des classes
Speaker = Speak(engine)
TimeSpeak = Time(datetime,Speaker)
TakeCommandS = TakeCommand(sr, Speaker)
SystemTask = System(datetime, os, random, psutil, pyautogui,Speaker)
JokeSpeaker = Joke(pyjokes, Speaker)
MailManage = Mail(smtplib)
Translation_lang = Translation(cur_lang)

#On se place dans le dossier system32 pour avoir accès a toutes les commandes
os.chdir("c:\Windows\system32")
path_data = "E:/MES PROJETS (programmation)/projest IA/IA_JORDI/"
path_data2 = "E:\\MES PROJETS (programmation)\\projest IA\\IA_JORDI\\"
   
#Début du programme
pause = False
program = True

#Salutation
TimeSpeak.salutation()
TimeSpeak.wishme()
while program == True:
    #Recupération de la commande 
    query = TakeCommandS.takeComand().lower()
    if "jordy" in query or "jordi" in query:
        pause = False
        Speaker.speak("Oui patron que puis-je faire pour vous ?")
    while pause == False:
        #Recupération de la commande 
        query = TakeCommandS.takeComand().lower()        
        #Changement de la langue
        if Translation_lang.changLang() in query:
            if cur_lang == 1:
                cur_lang = 0
                Translation_lang.setCurLang(0)
                Speaker.speak("Je m'exprime maintenant en français")
            else:
                cur_lang = 1
                Translation_lang.setCurLang(1)
                Speaker.speak("I will speak now in english")
            
        if "temps" in query:
            TimeSpeak.time()
        elif "date" in query:
            TimeSpeak.date()
        elif "wikipédia" in query:
            try:
                wikipedia.set_lang('fr')
                Speaker.speak("Recherche...")
                print("Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query,sentences=2)
                print(result)
                Speaker.speak(result)
            except Exception as e:
                print(e)
                Speaker.speak("Aucun resultat !")
        elif "envoi email" in query:
            try:
                Speaker.speak("Ques-ce que je dois dire ?")
                content = TakeCommandS.takeComand().lower()
                Speaker.speak("A qui ?")
                to = TakeCommandS.takeComand().lower() + "@gmail.com"
                print(to)
                MailManage.sendEmail(to,content)
                Speaker.speak("l'Email a été envoyer !")
                
            except Exception as e:
                print(e)
                Speaker.speak("Impossible d'envoyer l'email")

        elif "recherche dans chrome" in query:
            Speaker.speak("Ques-ce que je dois chercher Mr ?")    
            search = TakeCommandS.takeComand().lower()
            wb.get(path_pprog("chrome")).open_new_tab(search + '.com')
            
        elif "souviens-toi de" in query:
            date_remember = str(datetime.datetime.now().strftime("%d-%B-%Y  %H:%M"))
            os.defpath
            Speaker.speak("De quoi devrais-je me souvenir ?")
            data = TakeCommandS.takeComand().lower()
            Speaker.speak("Vous m'avez demander de me souvenir de la phrase :  "+ data)
            remember = open(path_data + '/data.txt','a')
            remember.write("\n" + date_remember + " " + data)
            remember.close()

        elif "Connais-tu quelque chose ?" in query:
            Speaker.speak("Vous m'avez demander de me souvenir de : ")    
            remember = open(path_data + '/data.txt','r')
            data = remember.read()
            print(data)
            Speaker.speak(data)
        elif "cpu" in query:
            SystemTask.cpu()
            
        elif "une blague" in query:
            JokeSpeaker.jokes()
            
        elif "screenshot" in query:
            SystemTask.screenshot(path_data2)
            Speaker.speak("Terminer !")
            
        elif "éteint l'ordi" in query:
            Speaker.speak("Je vais éteindre l'ordinateur dans 600 secondes")
            SystemTask.shutdown()
            
        elif "annule l'arrêt" in query:
            Speaker.speak("l'extinction a été annuler Mr.")
            SystemTask.noShutdonw()
            
        elif "redémarre le systeme" in query:
            Speaker.speak("Le systeme sera redemarrer dans 600 secondes ")
            SystemTask.reboot()
        
        elif "ton créateur" in query:
            texte = "Je suis un projet encore en développement. Mon créateur est un etudiant talentieux passionné par"
            texte += " l'informatique. Il se nome ANAFACK Didérot. Selon lui, actuelement je ne suis qu'a " 
            texte +="2 pourcent de mes possibilités et fonctionnalités."
            Speaker.speak(texte)
            
        elif "arrête d'écouter" in query:
            Speaker.speak("D'accord Mr ")
            pause = True
            break
        
        
        elif "repose-toi" in query:
            Speaker.speak("Aurevoir Patron.")
            program = False
            break
        
            
    if "repose-toi" in query:
        Speaker.speak("Aurevoir patron.")
        break
    
    

