import requests
from time import sleep
verifyversionatgithub= requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/databaseversion.txt")
getdatabase=requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/database.json")
getlistid=requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/listids.txt")
getpirateinstaller=requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/pirateinstaller.py")
with open("database.json","w") as databaseupd:
        databaseupd.write(getdatabase.text)
with open("databaseversion.txt","w") as versionupd:
    versionupd.write(verifyversionatgithub.text)
with open("listids.txt","w") as listid:
    listid.write(getlistid.text)
with open("pirateinstaller.py","w", encoding='utf-8') as pirateinstaller:
     pirateinstaller.write(getpirateinstaller.text)
print("updated with succesfull!")