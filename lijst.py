import json
import os
import webbrowser

def json_load(pad):
    try:
        with open(pad, "r") as f:
          return json.load(f)
    except FileNotFoundError:
        print("deze file wordt aangemaakt als je servers toevoegt")

def json_dump(pad,lijst):
    with open(pad,"w") as f:
        json.dump(lijst,f)

def deleteServer(server):
    serverlijst = json_load("serverdata")
    if server not in str(serverlijst):
        print("het opgegeven adres bestaat niet")
        input("druk op een toets om verder te gaan")
    else:
        for i in range(len(serverlijst)):
            if serverlijst[i][1][0] == server:
                del serverlijst[i]
        json_dump("serverdata", serverlijst)
    
def addServer(test, url, con1 = "n/a", con2 = "n/a"):
    if not os.path.isfile("serverdata"):
        serverlijst = []
        inhoud = ["test",["url", "con1", "con2"]]
        serverlijst.append(inhoud)
    else:
        serverlijst = json_load("serverdata")
    content = [test, [url, con1, con2]]
    serverlijst.append(content)
    json_dump("serverdata",serverlijst)
    
def generateHTML(pad,lijst):
    html_list = []
    pagina = False
    ping = False
    template = open(pad, "r")
    site = open("site/index.html", "w")
    while True:
        regel = template.readline()
        site.write(regel)
        if len(regel) == 0:
            break
        if regel == '    <div class="pagina">\n':
            pagina = True
        if regel == '    <div class="ping">\n':
            ping = True   
        if regel == '        <ul>\n':
            if pagina == True:
                for i in range(1, len(lijst)):
                    site.write(f'           <li>{lijst[i][1][0]}</li>\n')
                    pagina = False
            if ping == True:
                for i in range(1, len(lijst)):
                    site.write(f'           <li>{lijst[i][1][1]}</li>\n')
                    ping = False 
    template.close()
    site.close()
    filename = 'file://'+os.getcwd()+'/' + 'site' + '/' + 'index.html'
    print(filename)
    webbrowser.open_new_tab(filename)









     

            


