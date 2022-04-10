import requests, sys, subprocess

def currentPath():

    windowsUser = subprocess.getoutput('echo %username%')

    with requests.session() as session:

        windowsPlayer = session.get(
            'https://clientsettings.roblox.com/v2/client-version/WindowsPlayer'
        )

    path = [

        f'C:\\Users\\{windowsUser}\\AppData\\Local\\Roblox\\Versions\\' + windowsPlayer.json()['clientVersionUpload']

    ]

    
    path = path[0]

    return path


if __name__ == '__main__':

    arguments = sys.argv[1:]

    for arg in arguments:

        if arg == '.path':
            path = currentPath()
            print(path)
            