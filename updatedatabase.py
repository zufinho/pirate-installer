import requests
from time import sleep
with open("databaseversion.txt","r") as ver:
    version = ver.read()
verifyversionatgithub= requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/databaseversion.txt")
if not version != verifyversionatgithub:
    getdatabase=requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/database.json")
    with open("database.json","w") as databaseupd:
        databaseupd.write(getdatabase)
    with open("databaseversion.txt","w") as versionupd:
        versionupd.write(verifyversionatgithub)
    print("updated with succesfull!")
else:
    print("not update needs")
sleep(5)