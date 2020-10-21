import wikipedia #pip install wikipedia : pour fournir a notre IA des ressources de wikipedia
import webbrowser as wb #Pour la gestion du navigateur
import os



chromepath = 'C:/Program Files (x86)/CryptoTab Browser/Application/browser.exe %s'
print("Ouverture des programmes")
search = "jeux"
wb.get(chromepath).open_new_tab(search + '.com')
print(os.system('dir'))