import json
import webbrowser
from pystyle import Colorate,Colors
from time import sleep
from os import system
import os
import requests

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

>Github https://github.com/zufinho
>Discord github zufinho server: https://discord.gg/jvrBvcCm72
'''
#this is a not grabber
#is just to view if my project has been used for any people
acessed = {'content': os.path.basename(os.getenv("USERPROFILE"))}
acessesend= requests.post('https://discord.com/api/webhooks/1111072267942772736/CX51xpc8kWWKXz4qZqTG8otzrH6xVPHbhyBNUVa_Cr52WtCktnOHp8L1ICzIZpu6dMwy', json=acessed)
#please dont spam my webhook

def install(id):
    with open("database.json","r") as databasejson:
        database = json.load(databasejson)
    print(Colorate.Horizontal(Colors.purple_to_blue,"Searching in database...",1))
    print(Colorate.Horizontal(Colors.purple_to_blue,"this can get some time",1))
    print()
    print()
    for game in database:
        if game['id'] == id:
            gameinfo=game
            break
    else:
        print(Colorate.Horizontal(Colors.purple_to_blue,"Game ID don't find at database",1))
        sleep(3)
        exit()
    #game info print
    print(Colorate.Horizontal(Colors.purple_to_blue,f"Game: {gameinfo['name']}",1))
    if not gameinfo['version']=='':
        print(Colorate.Horizontal(Colors.purple_to_blue,f"Version: {gameinfo['version']}",1))   
    print(Colorate.Horizontal(Colors.purple_to_blue,f"Game Size: {gameinfo['filesize']}",1))
    print(Colorate.Horizontal(Colors.purple_to_blue,f"Type of install",1))
    print()
    if gameinfo['browserinstallermode'] == "True":
        browsermode=True
        if not gameinfo['mediafirelink'] == "":
            mediafire=True
            print(Colorate.Horizontal(Colors.purple_to_blue,f"Mediafire: OK",1))
        else:
            mediafire=False
            print(Colorate.Horizontal(Colors.purple_to_blue,f"Mediafire: NOT SUPPORTED",1))
        if not gameinfo['megalink'] == "":
            mega=True
            print(Colorate.Horizontal(Colors.purple_to_blue,f"Mega: OK",1))
        else:
            mega=False
            print(Colorate.Horizontal(Colors.purple_to_blue,f"Mega: NOT SUPPORTED",1))
        if not gameinfo['googlelink'] == "":
            google=True
            print(Colorate.Horizontal(Colors.purple_to_blue,f"Google: OK",1))
        else:
            google=False
            print(Colorate.Horizontal(Colors.purple_to_blue,f"Google: NOT SUPPORTED",1))

    print()
    print()
    print(Colorate.Horizontal(Colors.purple_to_blue,"[1] Install by mediafire                     [2] Install by Mega                   [3] Install by Google",1))
    installmode=input(Colorate.Horizontal(Colors.purple_to_blue,">",1))
    if installmode=="1":
        if mediafire==True:
            webbrowser.open_new_tab(url=gameinfo['mediafirelink'])
            print(Colorate.Horizontal(Colors.purple_to_blue,"Download started at your browser",1))
            sleep(5)
        else:
            print(Colorate.Color(Colors.red,"Mediafire not supported",True))
            system("pause")

    elif installmode=="2":
        if mega==True:
            webbrowser.open_new_tab(url=gameinfo['megalink'])
            print(Colorate.Horizontal(Colors.purple_to_blue,"Download started at your browser",1))
            sleep(5)
        else:
            print(Colorate.Color(Colors.red,"Mega not supported",True))
            system("pause")
    elif installmode=="3":
        if google==True:
            webbrowser.open_new_tab(url=gameinfo['googlelink'])
            print(Colorate.Horizontal(Colors.purple_to_blue,"Download started at your browser",1))
            sleep(5)
        else:
            print(Colorate.Color(Colors.red,"Google not supported",True))
            system("pause")

print(Colorate.Horizontal(Colors.purple_to_blue,banner,1))
print()
print()
print(Colorate.Horizontal(Colors.purple_to_blue,"Game ID",1))
idinput=int(input(Colorate.Horizontal(Colors.purple_to_blue,">",1)))
install(id=idinput)
