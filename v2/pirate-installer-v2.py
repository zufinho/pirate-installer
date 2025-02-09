#made and scripted by zufinho
#v2 becomming better and more easier to find your games :)
import json
from os import system, name as osname
from time import sleep
try:
    import requests
    from pystyle import Colorate, Colors
except:
    print('Installing dependencies...')
    print()
    system('pip install requests pystyle')
finally:
    import requests
    from pystyle import Colorate, Colors
system('cls') if osname == 'nt' else system('clear')
print('Verifing connection with network...')
print()
while True:
    try:
        requests.get("https://google.com")
        break
    except:
        print("No connection with network, trying again...")

#verify updates
version=open('src/version')
version=version.read().strip()
dbversion=open('src/dbversion','r')
dbversion=dbversion.read().strip()
gitversion = requests.get('https://raw.githubusercontent.com/zufinho/pirate-installer/refs/heads/main/v2/src/version').text.strip()
gitdbversion = requests.get('https://raw.githubusercontent.com/zufinho/pirate-installer/refs/heads/main/v2/src/dbversion').text.strip()
if version!=gitversion:
    print('New client installer avaible, install? (y/n)')
    cmd=input(">")
    go=0
    try:
        cmd=str(cmd)
        go=1
    except:
        print('Insert only letters')
    if go==1:
        if cmd.lower()=='y':
            program=requests.get('https://raw.githubusercontent.com/zufinho/pirate-installer/refs/heads/main/v2/pirate-installer-v2.py').text
            with open('pirate-installer-v2.py','w') as file:
                file.write(program)
            with open('src/version','w') as file:
                file.write(gitversion)
            print('Client updated!')
            sleep(1)
            if osname=='nt':
                system('python pirate-installer-v2.py')
            else:
                system('python3 pirate-installer-v2.py')
            del program
            exit()
if dbversion!=gitdbversion:
    print('New games database update avaible, install? (y/n)')
    cmd=input(">")
    go=0
    try:
        cmd=str(cmd)
        go=1
    except:
        print('Insert only letters')
    if go==1:
        if cmd.lower()=='y':
            gitdb=requests.get('https://raw.githubusercontent.com/zufinho/pirate-installer/refs/heads/main/v2/src/games.json').text
            with open('src/games.json','w') as file:
                file.write(gitdb)
            with open('src/dbversion','w') as file:
                file.write(gitdbversion)
            print('Games database updated!')
            sleep(1)
            del gitdb

del gitdbversion, gitversion

def printcolor(text,end="\n"):
    print(Colorate.Horizontal(Colors.blue_to_purple,text,1),end=end)
def printerror(text):
    print(Colorate.Color(Colors.red,text,1))
def printgreen(text):
    print(Colorate.Color(Colors.green,text,1))
def clear():
    if osname=="nt":
        system("cls")
    else:
        system("clear")
banner=r'''
 ______ _                         _                      _ _             
(_____ (_)           _           (_)           _        | | |            
 _____) )  ____ ____| |_  ____    _ ____   ___| |_  ____| | | ____  ____ 
|  ____/ |/ ___) _  |  _)/ _  )  | |  _ \ /___)  _)/ _  | | |/ _  )/ ___)
| |    | | |  ( ( | | |_( (/ /   | | | | |___ | |_( ( | | | ( (/ /| |    
|_|    |_|_|   \_||_|\___)____)  |_|_| |_(___/ \___)_||_|_|_|\____)_|    


>Made and Scripted by zufinho
>https://github.com/zufinho'''
#script starts


db=open('src/games.json','r')
dbj=json.load(db)
if osname=="nt":
    system('title Pirate Installer')

def listofgames():
    a=0
    for game in dbj:
        printcolor(f'{a}: {game['gamename']}')
        a+=1

def searchgame(name):
    go=0
    try:
        name=str(name)
        go=1
    except:
        printerror('Please insert only string')
        sleep(3)
    if name=="" or name==" ":
        printerror("Insert game name!")
        sleep(3)
        go=0
    if go==1:
        printcolor(f'Searching games with name "{name}"')
        name=name.lower()
        found=0
        founds=[]
        for game in dbj:
            a=str(game['gamename']).lower()
            a=a.find(name)
            if a==0 or a>0:
                found+=1
                founds.append(game['id'])
            printcolor(f'{found} Games Found', end="\r")
        print("\n")
        if found>0:
            for game in founds:
                for gm in dbj:
                    if gm['id'] == game:
                        printcolor(f'Name: {gm['gamename']}')
                        printcolor(f'ID: {game}')
                        versions=0
                        for v in gm['game']['versions']:
                            versions+=1
                        printcolor(f'Q. Versions: {versions}')
                        print()
        else:
            printerror('No games found.')
        input('Press any key to continue')

def getgame(id):
    found=0
    printcolor('Searching for game id...')
    for game in dbj:
        if game['id']==id:
            found=1
            gamejson=game
            printgreen('Game Found!\n')
            break
    if found==1:
        sleep(1.5)
        return gamejson
    else:
        printerror('Game not found!\n')
        sleep(1.5)
        return False

def getversions(gamejson,versionn):
    versions=gamejson['game']['versions']
    return versions[versionn]


def main():
    gamecount=0
    for game in dbj:
        gamecount+=1
    def printinitial():
        printcolor(banner)
        printcolor(f">Version {version}")
        printcolor(f">{gamecount} Games in total")
        print()
        print()

    while True:
        clear()
        printinitial()
        printcolor('[1] Get game           [2] List of games           [3] Search game')
        printcolor("[98] Help              [99] Exit")
        cmd=input(">")
        if cmd=="1":
            printcolor('Insert game ID')
            cmd=input(">")
            clear()
            printinitial()
            go=0
            try:
                cmd=int(cmd)
                go=1
            except:
                go=0
                printerror('Insert only numbers!')
                sleep(3)
            if go==1:
                    game=getgame(cmd)
                    if game==False:
                        print()
                    else:
                        gameversioncount=0
                        gameversions=[]
                        gameversionsprint=[]
                        for gversion in game['game']['versions']:
                            gameversioncount+=1
                            gameversions.append(gversion)
                            gameversionsprint.append(f"Version {gameversioncount}:\nVersion: {gversion['version']}\nDLC: {gversion['dlc']}\nLength: {gversion['gamelength']}\nAdded to client in: {gversion['dateadded']}")
                        while True:
                            clear()
                            printinitial()
                            printcolor(F'Game: {game['gamename']}')
                            printcolor(f'{gameversioncount} Versions:')
                            print()
                            for g in gameversionsprint:
                                printcolor(g)
                                print()
                            print()
                            printcolor('[1] Select Version and install      [99] Back')
                            cmd=input(">")
                            if cmd=="1":
                                printcolor('Select your version:')
                                cmd=input(">")
                                go=0
                                try:
                                    cmd=int(cmd)
                                    go=1
                                except:
                                    printerror('Insert only numbers!')
                                    sleep(1.5)
                                if go==1:
                                    if cmd<=0 or cmd>gameversioncount:
                                        printerror('Insert a valid version!')
                                        sleep(1.5)
                                    else:
                                        gameversion=getversions(game,cmd-1)
                                        clear()
                                        printinitial()
                                        txt=f'''Game: {game['gamename']}
        Version: {gameversion['version']}
        DLC: {gameversion['dlc']}
        Length: {gameversion['gamelength']}
        Date Added to client: {gameversion['dateadded']}
        Link to Download: {gameversion['downloadlink']}
        '''
                                        printcolor(txt)
                                        input('Press any key to continue...')
                                        break
                            elif cmd=="99":
                                cmd=None
                                break

        elif cmd=="2":
            clear()
            printinitial()
            printcolor("ID: GAMENAME")
            listofgames()
            print()
            input("Press any key to continue...")
        elif cmd=="3":
            clear()
            printinitial()
            printcolor("Insert game name to search:")
            cmd=input(">")
            clear()
            printinitial()
            searchgame(cmd)
        
        elif cmd=='98':
            clear()
            printinitial()
            printcolor("What's is this program?")
            printcolor('This program is a client to download games, having a "database" with games and their download links, ALL THE GAMES IS TESTED!')
            print()
            printcolor("How it's work?")
            printcolor("It's works with IDs, every game have an ID, you can see at searching by game name or in list of games, to get a link of download from any game u need the game id.")
            print()
            printcolor("I can use other database?")
            printcolor("Yes! u can use other database created by you or other people, but caution to no get malwares!")
            printcolor('U can view how the database is created in src/basegames.json')
            print()
            input('Press any key to continue')
        elif cmd=="99":
            clear()
            db.close()
            exit(0)
if __name__ == "__main__":
    main()