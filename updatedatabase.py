import requests
from time import sleep
with open("databaseversion.txt","r") as ver:
    version = ver.read()
verifyversionatgithub= requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/databaseversion.txt")
if not version == verifyversionatgithub:
    getdatabase=requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/database.json")
    getlistid=requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/listids.txt")
    with open("database.json","w") as databaseupd:
        databaseupd.write(getdatabase.text)
    with open("databaseversion.txt","w") as versionupd:
        versionupd.write(verifyversionatgithub.text)
    with open("listids.txt","w") as listid:
        listid.write(getlistid.text)
    print("updated with succesfull!")
else:
    print("not update needs")
sleep(5)