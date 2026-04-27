reihe0 = [" ", "1", "2", "3"]
reihe1 = ["A", ".", ".", "."]
reihe2 = ["B", ".", ".", "."]
reihe3 = ["C", ".", ".", "."]

def zeichneFeld():
    print(reihe0)
    print(reihe1)
    print(reihe2)
    print(reihe3)

def reihe1Ändern(spaltenWahl, spieler):
    global zugGespielt

    if reihe1[spaltenWahl] == ".":
        reihe1[spaltenWahl] = spieler
        guckObGewonnen(spieler)
        zugGespielt = True
    else:
        print("Da steht schon was. ")

def reihe2Ändern(spaltenWahl, spieler):
    global zugGespielt

    if reihe2[spaltenWahl] == ".":
        reihe2[spaltenWahl] = spieler
        guckObGewonnen(spieler)
        zugGespielt = True
    else:
        print("Da steht schon was. ")

def reihe3Ändern(spaltenWahl, spieler):
    global zugGespielt

    if reihe3[spaltenWahl] == ".":
        reihe3[spaltenWahl] = spieler
        guckObGewonnen(spieler)
        zugGespielt = True
    else:
        print("Da steht schon was. ")

def spielerAnzeige(spieler):
    print(f"Spieler '{spieler}' ist an der Reihe")

def zähler(zähler):
    global gewonnen

    if zähler == 3:
        gewonnen = True


def guckObGewonnen(spieler):
    global gewonnen
    aktuellerZähler = 0

    for i in reihe1:

        if i == spieler:
            aktuellerZähler += 1

    zähler(aktuellerZähler)
    aktuellerZähler = 0

    for i in reihe2:

        if i == spieler:
            aktuellerZähler += 1

    zähler(aktuellerZähler)
    aktuellerZähler = 0

    for i in reihe3:
        if i == spieler:
            aktuellerZähler += 1

    zähler(aktuellerZähler)

    if reihe1[1] == reihe2[1] == reihe3[1] == spieler:
        gewonnen = True
    elif reihe1[2] == reihe2[2] == reihe3[2] == spieler:
        gewonnen = True
    elif reihe1[3] == reihe2[3] == reihe3[3] == spieler:
        gewonnen = True

    if reihe1[1] == reihe2[2] == reihe3[3] == spieler:
        gewonnen = True
    elif reihe1[3] == reihe2[2] == reihe3[1] == spieler:
        gewonnen = True


spieler = "x"
zugGespielt = False
gewonnen = False

while True:

    zeichneFeld()

    if gewonnen:
        print(f"{spieler} hat gewonnen!")
        break

    if spieler == "o" and zugGespielt == True:
        spieler = "x"
        zugGespielt = False
    elif spieler == "x" and zugGespielt == True:
        spieler = "o"
        zugGespielt = False

    spielerAnzeige(spieler)

    zeilenWahl = input("In welcher Zeile möchtest du dein Zeichen setzen? (A, B, C): ")
    spaltenWahl = int(input("In welcher Spalte möchtest du dein Zeichen setzen? (1, 2, 3): "))

    #AuswahlZeileSpalte
    if zeilenWahl.upper() == "A":
        if spaltenWahl >=1 and spaltenWahl <= 3:
            reihe1Ändern(spaltenWahl, spieler)
        else:
            print("Gib eine Nummer zwischen 1 und 3 ein.")
            continue

    elif zeilenWahl.upper() == "B":
        if spaltenWahl >= 1 and spaltenWahl <= 3:
            reihe2Ändern(spaltenWahl, spieler)
        else:
            print("Gib eine Nummer zwischen 1 und 3 ein.")
            continue

    elif zeilenWahl.upper() == "C":
        if spaltenWahl >= 1 and spaltenWahl <= 3:
            reihe3Ändern(spaltenWahl, spieler)
        else:
            print("Gib eine Nummer zwischen 1 und 3 ein.")
            continue

    else:
        print("Gib eine gültige Zeile ein.")
        continue
