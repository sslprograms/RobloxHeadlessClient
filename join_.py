import requests, json, sys, random, subprocess


# robloxplayerbeta.exe -a "https://www.roblox.com/Login/Negotiate.ashx" -t {t} -j {j}
# Disabled because the JoinScriptUrl won't work ;(

headers = {
    'User-Agent':'Roblox\Winlet'
}

def requestJoin(cookie, placeId):

    with requests.session() as session:

        session.cookies['.ROBLOSECURITY'] = cookie
        session.headers = headers


        browserId=random.randint(10000,1000000)

        joinData = session.post(
            f'https://assetgame.roblox.com/game/PlaceLauncher.ashx?request=RequestPrivateGame&browserTrackerId={browserId}&placeId={placeId}&isPlayTogetherGame=false&accessCode=36e9d1f4-55d2-48ea-8af9-25f220829179&linkCode=',
        )


        ticket = subprocess.getoutput(f'_auth.py "{cookie}" {placeId}').split(',')
        ticket = ticket[0]
        username = ticket[1]
        
        if joinData.json()['jobId'] != None:

            while True:

                joinScript = joinData.json()['joinScriptUrl']
                A_url = joinData.json()['authenticationUrl']
                gameId = joinData.json()['jobId']

                requestGame = session.post(
                    'https://gamejoin.roblox.com/v1/join-game',
                    data = {
                        'gameId':gameId,
                        'browserTrackerId':browserId,
                        'isTeleport':False,
                        'isPartyLeader':False,
                        'isPlayTogetherGame':False,
                        'placeId':placeId
                    }
                )

                if requestGame.json()['joinScriptUrl'] != None:

                    joinscripturl = requestGame.json()['joinScriptUrl']


                    launchNote = f'gameJoin.exe --play --fast  -a "https://www.roblox.com/Login/Negotiate.ashx" -t "{ticket}" -j "https://assetgame.roblox.com/game/PlaceLauncher.ashx?request=RequestGame&browserTrackerId={browserId}&placeId={placeId}&isPartyLeader=false" -b 123' + ' +,+ ' + username
                    print(launchNote)

                    break



if __name__ == '__main__':
    arguments = sys.argv[1:]

    # extr = {}

    # for arg in arguments:

    #     if arg.replace('.place=',''):

    #         place = arg.replace('.place=','')

    #         try:

    #             place = int(place)
    #             data = {
    #                 'place':place
    #             }
    #             extr.update(data)
    #         except:
    #             pass

    #     if arg.replace('.cookie=', ''):

    #         cookie = arg.replace('.cookie=', '')

    #         try:

    #             cookie = str(cookie)
    #             data = {
    #                 'cookie':cookie
    #             }
    #             extr.update(cookie)
            
    #         except:
    #             pass

    
    # requestJoin(extr['cookie'], extr['place'])
    requestJoin(arguments[0], arguments[1])



