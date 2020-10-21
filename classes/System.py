class System():
    """ Cette classe contient toutes les methodes pour interagir avec le systeme """
    
    def __init__(self, datetime, os, random, psutil, pyautogui, speak):
        self.datetime = datetime
        self.os = os
        self.random = random
        self.psutil = psutil
        self.pyautogui = pyautogui
        self.speak = speak.speak
        
    def shutdown(self):
        self.os.system("shutdown -s -t 600")

    def noShutdonw(self):
        self.os.system("shutdown -a")

    def reboot(self):
        self.os.system("shutdown -r -t 600")
    
    def screenshot(self, path_data2):
        img = self.pyautogui.screenshot()
        auto = str(self.random.randint(0,1000))
        img.save(path_data2 + "screenshot\\ss"+auto+".png")

    def cpu(self):
        usage = str(self.psutil.cpu_percent())
        self.speak("CPU is at "+ usage)
        battery = self.psutil.sensors_battery()
        self.speak("Battery is at ")
        self.speak(battery.percent)

        