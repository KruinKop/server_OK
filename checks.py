from ping3 import ping
import lijst

def pingCheck():
    servers = lijst.json_load("serverdata")
    for i in range(1,len(servers)):
        resp = ping(servers[i][1][0],unit='ms')
        servers[i][1][1] = resp
        lijst.json_dump("serverdata",servers)
    lijst.generateHTML("site/index_templ.html", servers)
    

    