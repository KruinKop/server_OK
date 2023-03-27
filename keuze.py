import json
import rich
from rich import print

def anyKey():
    print("\n")
    input("druk op een toets om verder te gaan")

def showList(lijst):
    try:
        with open(lijst, "r") as f:
                dataset = json.load(f)
                print(dataset)
                anyKey()
    except FileNotFoundError:
        print("deze file is nog niet aangemaakt")
        anyKey()
        
def wachtwoord(user):
    isAdmin = False
    if user == "Admin":
        ww = input("geef het wachtwoord in, geef 0 in als je het niet weet ")
        while True:
            if ww == "server":
                print("het wachtwoord is juist")
                isAdmin = True
                break
            elif ww == "0":
                break
            else:
                print("geef opnieuw het wachtwoord in ")
    return isAdmin

def keuzemenu():
    import lijst
    import os
    import checks

    while True:
        os.system('clear')
        print("[bold magenta]kies uit de volgende opties[/bold magenta]\n1) [i]lijst openen[/i]\n2) [i]adres toevoegen[/i]\n3) [i]adres verwijderen[/i]\n4) [i]test[/i] \n0) [i]programma stoppen[/i]")
        keuze = int(input())

        match keuze:
            case 1:
                showList("serverdata")
            case 2:
                test = input("welke test wil je uitvoeren? ")
                url = input("welk domein wil je testen? ")
                lijst.addServer(test,url)         
            case 3:
                te_verwijderen = input("welk adres wil je van de lijst verwijderen? ")
                lijst.deleteServer(te_verwijderen)
            case 4:
                checks.pingCheck()
            case 0:
                break


