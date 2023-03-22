import sys
import keuze

admin = False

if len(sys.argv) > 1:
    admin = keuze.wachtwoord(sys.argv[1])   
    
else:
    keuze.keuzemenu()