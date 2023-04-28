import json
import webbrowser
from pystyle import Colorate,Colors
from time import sleep
from os import system

banner='''

██████╗░██╗██████╗░░█████╗░████████╗███████╗
██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██████╔╝██║██████╔╝███████║░░░██║░░░█████╗░░
██╔═══╝░██║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░
██║░░░░░██║██║░░██║██║░░██║░░░██║░░░███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝

██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░███████╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔══██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░█████╗░░██████╔╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗███████╗██║░░██║
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝
'''


def install(id):
    with open("database.json","r") as databasejson:
        database = json.load(databasejson)
    print(Colorate.Horizontal(Colors.blue_to_cyan,"Searching in database...",1))
    print(Colorate.Horizontal(Colors.blue_to_cyan,"this can get some time",1))
    print()
    print()
    for game in database:
        if game['id'] == id:
            gameinfo=game
            break
    else:
        print(Colorate.Horizontal(Colors.blue_to_cyan,"Game ID don't find at database",1))
        sleep(3)
        exit()
    #game info print
    print(Colorate.Horizontal(Colors.blue_to_cyan,f"Game: {gameinfo['name']}",1))
    if not gameinfo['version']=='':
        print(Colorate.Horizontal(Colors.blue_to_cyan,f"Version: {gameinfo['version']}",1))   
    print(Colorate.Horizontal(Colors.blue_to_cyan,f"Game Size: {gameinfo['filesize']}",1))
    print(Colorate.Horizontal(Colors.blue_to_cyan,f"Type of install",1))
    print()
    if gameinfo['browserinstallermode'] == "True":
        browsermode=True
        if not gameinfo['mediafirelink'] == "":
            mediafire=True
            print(Colorate.Horizontal(Colors.blue_to_cyan,f"Mediafire: ✅",1))
        else:
            mediafire=False
            print(Colorate.Horizontal(Colors.blue_to_cyan,f"Mediafire: ❌",1))
        if not gameinfo['megalink'] == "":
            mega=True
            print(Colorate.Horizontal(Colors.blue_to_cyan,f"Mega: ✅",1))
        else:
            mega=False
            print(Colorate.Horizontal(Colors.blue_to_cyan,f"Mega: ❌",1))
        if not gameinfo['anonfileslink'] == "":
            anon=True
            print(Colorate.Horizontal(Colors.blue_to_cyan,f"Anonfiles: ✅",1))
        else:
            anon=False
            print(Colorate.Horizontal(Colors.blue_to_cyan,f"Anonfiles: ❌",1))

    print()
    print()
    print(Colorate.Horizontal(Colors.blue_to_cyan,"[1] Install by mediafire                     [2] Install by Mega                   [3] Install by AnonFiles",1))
    print(Colorate.Horizontal(Colors.blue_to_cyan,"[4] Open Mediafire game download page        [5] Open Mega game download page      [6] Open Anonfiles game download page",1))
    installmode=input(Colorate.Horizontal(Colors.blue_to_cyan,">",1))
    if installmode=="1":
        if mediafire==True:
            webbrowser.open_new_tab(url=gameinfo['mediafiredownloadlink'])
            print(Colorate.Horizontal(Colors.blue_to_cyan,"Download started at your browser",1))
            sleep(5)
        else:
            print(Colorate.Color(Colors.red,"Mediafire not supported",True))
            system("pause")

    elif installmode=="2":
        if mega==True:
            webbrowser.open_new_tab(url=gameinfo['megadirectdownload'])
            print(Colorate.Horizontal(Colors.blue_to_cyan,"Download started at your browser",1))
            sleep(5)
        else:
            print(Colorate.Color(Colors.red,"Mega not supported",True))
            system("pause")
    elif installmode=="3":
        if anon==True:
            webbrowser.open_new_tab(url=gameinfo['anondirectdownload'])
            print(Colorate.Horizontal(Colors.blue_to_cyan,"Download started at your browser",1))
            sleep(5)
        else:
            print(Colorate.Color(Colors.red,"Anonfiles not supported",True))
            system("pause")
    elif installmode=="4":
        if mediafire==True:
            webbrowser.open_new_tab(url=gameinfo['mediafirelink'])
            print(Colorate.Horizontal(Colors.blue_to_cyan,"Opened in your browser",1))
            sleep(5)
        else:
            print(Colorate.Color(Colors.red,"Mediafire not supported",True))
            system("pause")
    elif installmode=="5":
        if mega==True:
            webbrowser.open_new_tab(url=gameinfo['megalink'])
            print(Colorate.Horizontal(Colors.blue_to_cyan,"Opened in your browser",1))
            sleep(5)
        else:
            print(Colorate.Color(Colors.red,"Mega not supported",True))
            system("pause")
    elif installmode=="6":
        if anon==True:
            webbrowser.open_new_tab(url=gameinfo['anonfileslink'])
            print(Colorate.Horizontal(Colors.blue_to_cyan,"Opened in your browser",1))
            sleep(5)
        else:
            print(Colorate.Color(Colors.red,"Anonfiles not supported",True))
            system("pause")

print(Colorate.Horizontal(Colors.blue_to_cyan,banner,1))
print()
print()
print(Colorate.Horizontal(Colors.blue_to_cyan,"Game ID",1))
idinput=int(input(Colorate.Horizontal(Colors.cyan_to_blue,">",1)))
install(id=idinput)