import requests, sys

def getAuthenticationTicket(cookie):

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44',
        'referer':'https://www.roblox.com/',
        'origin':'https://www.roblox.com'
    }


    with requests.session() as session:
        session.cookies['.ROBLOSECURITY'] = cookie
        session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
        auth_ticket = session.post(
            'https://auth.roblox.com/v1/authentication-ticket/',
            headers=headers
        )

        username = session.get(
            'https://users.roblox.com/v1/users/authenticated'
        ).json()['name']

        print(auth_ticket.headers['rbx-authentication-ticket']+','+username)

    return


if __name__ == '__main__':
    arguments = sys.argv[1:]

    getAuthenticationTicket(arguments[0])