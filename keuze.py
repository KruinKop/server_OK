def keuzemenu():
    while True:
        print("kies uit de volgende opties\n1) lijst openen\n2) adres toevoegen\n3) adres verwijderen\n0) programma stoppen")
        keuze = int(input())

        match keuze:
            case 1:
                print("we gaan de lijst openen")
            case 2:
                print("we gaan een adres toevoegen")
            case 3:
                print("we gaan een adres verwijderen")
            case 0:
                break

def wachtwoord(user):
    if user == "Admin":
        ww = input("geef het wachtwoord in, geef 0 in als je het niet weet ")
        while True:
            if ww == "server":
                print("het wachtwoord is juist")
                return True
            elif ww == "0":
                break
            else:
                print("geef opnieuw het wachtwoord in")
    return False
