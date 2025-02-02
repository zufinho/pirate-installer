import os
try:
    import cloudscraper
except:
    os.system('pip install cloudscraper')
    import cloudscraper
import threading
import json
scraper = cloudscraper.create_scraper()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
def check(url,gameid,gamename):
    site=scraper.get(url,headers=headers,allow_redirects=True)
    if site.status_code==429:
        print(f'{gameid}:{gamename} | Too many requests')
    elif site.status_code==200:
        print(f'{gameid}:{gamename} | OK')
    else:
        print(f'{gameid}:{gamename} | DOWN')

print('Checking...')
with open('database.json','r') as file:
    db=json.load(file)
    for game in db:
        if game['mediafirelink'] == '':
            pass
        else:
            checke=threading.Thread(target=check,args=(game['mediafirelink'],game['id'],game['name'],)).start()
while threading.active_count()>1:
    z=0
input('Press any key to contiue.')
