import time

horloge_active = True
#Horloge manuelle#
def horloge(hour, minute, second):
    while horloge_active:
        if second > 59:
            second = 0
            minute += 1
        if minute > 59:
            minute = 0
            hour += 1
        if hour > 23:
            hour = 0
            minute = 0
            second = 0
        if hour == 0 and minute == 0 and second == 5:
            print("Alarme!")
            time.sleep(1)
        print("{:02d}:{:02d}:{:02d}".format(hour, minute, second))
        second += 1
        time.sleep(1) 
#Il faut supprimer la ligne horloge pour lancer l'horloge automatique#
horloge (20, 18, 0)
heure_actuelle = (16, 30, 0)
#heure alarme horloge manuelle#
alarme = (0, 0, 0)

#Horloge Automatique#
def afficher_heure():
    global horloge_active
    horloge_active = False
    heures, minutes, secondes = heure_actuelle
    print(f"{heures:02d}:{minutes:02d}:{secondes:02d}")

def regler_alarme(nouvelle_alarme):
    global alarme
    alarme = nouvelle_alarme

while True:
    afficher_heure()
    if heure_actuelle == alarme:
        print("Alarme!")
    time.sleep(1)
    heure_actuelle = time.localtime()[3:6]
    #heure a rentre pour l'alarme de l'horloge auto#
    alarme = (9, 37, 0)
    