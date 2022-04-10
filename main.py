import subprocess, os, threading, colorama, win32event, pygetwindow, time
import requests
import sys


def checkFiles():

    if os.path.exists('accounts'):

        try:

            accounts = open('accounts\\accounts.txt', 'r').read().splitlines()
            return accounts

        except:

            print(colorama.Fore.WHITE + ':: Anatomy could not find the (accounts.txt) in the [accounts] directory.')
            quit()

    else:

        print(colorama.Fore.WHITE + ':: Anatomy could not find the (accounts) directory')
        quit()


accounts = checkFiles()

def keep_connection():

    subprocess.getoutput('_keep_con.py .loop')

threading.Thread(target=keep_connection,).start()
TOTAL = 0
def launch_instance(sig, path):
    global TOTAL
    subprocess.getoutput(f'path\\{sig}')
    TOTAL -= 1
    print(f'::- Roblox client has disconnected from the game. [{TOTAL}]')


    


def handle(cookie, placeId):
    global TOTAL

    generate_launch_token = subprocess.getoutput(f'join_.py "{cookie}" "{placeId}"').split('+,+')

    username = requests.get(
        'https://users.roblox.com/v1/users/authenticated',

        cookies = {
            '.ROBLOSECURITY':cookie
        }
    ).json()['name']
    TOTAL += 1

    print(f'::- Roblox bot is joining the game. [Connected: {TOTAL}] ')

    launch_instance(generate_launch_token[0], '')



def main(placeId, threads, bots):
    print(colorama.Fore.WHITE  +'===========================================================================')

    print(colorama.Fore.LIGHTWHITE_EX + '''
                       _                               ___       
     /\               | |                             / _ \      
    /  \   _ __   __ _| |_ ___  _ __ ___  _   _ _____| (_) |_  __
   / /\ \ | '_ \ / _` | __/ _ \| '_ ` _ \| | | |______\__, \ \/ /
  / ____ \| | | | (_| | || (_) | | | | | | |_| |        / / >  < 
 /_/    \_\_| |_|\__,_|\__\___/|_| |_| |_|\__, |       /_/ /_/\_\
                                           __/ |                 
                                          |___/                  
''')
    print(colorama.Fore.WHITE  +'===========================================================================')
    ccnt = 0
    for x in range(int(bots)):
        time.sleep(0.05)
        
        if ccnt == int(threads):
            ccnt = 0            
            time.sleep(30)

        account = '_|' + accounts[x].split('_|')[1]
        threading.Thread(target=handle, args=(account,placeId,)).start()
        ccnt += 1
    input()
    subprocess.getoutput('taskkill /f /im gameJoin.exe')
    quit()



instance = win32event.CreateMutex(None, 1, "ROBLOX_singletonMutex")
arguments = sys.argv[1:]

main(arguments[0], arguments[1], arguments[2])