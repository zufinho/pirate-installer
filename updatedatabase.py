import requests
with open("databaseversion.txt","r") as ver:
    version = ver.read()
verifyversionatgithub= requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/databaseversion.txt")
if verifyversionatgithub != version:
    getdatabase=requests.get("https://raw.githubusercontent.com/zufinho/pirate-installer/main/database.json")
    print(getdatabase.text)