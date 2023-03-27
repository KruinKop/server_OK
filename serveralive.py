import sys
import keuze
import lijst
import checks

admin = False
'''
 terminal argumenten:
     1: admin/check
     2: keuze 1/2/3
        1: server toevoegen
        2: wissen
        3: lijst tonen
        4: test
     3: servernaam
     4: testsoort
'''

if len(sys.argv) > 1:
    admin = keuze.wachtwoord(sys.argv[1])   #admin controle
    if sys.argv[2] == str(3):
        keuze.showList("serverdata")
    elif sys.argv[2] == str(4):
        checks.pingCheck()
    if admin == True:
        if sys.argv[2] == str(1):
            lijst.addServer(sys.argv[4], sys.argv[3])
        elif sys.argv[2] == str(2):
            lijst.deleteServer(sys.argv[3])
        
else:
    keuze.keuzemenu()
