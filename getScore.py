import requests
from bs4 import BeautifulSoup
from googletrans import Translator


#Initializing instance of translator
translator = Translator()


headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}


#Function that takes in NBA team as argument and scrapes the web to find score
def getScore(team):
    switcher = {
        'LAL': 'http://www.google.com/search?q=lakers+latest+game&oq=lakers+latest+game&aqs=chrome..69i57.6290j0j9&sourceid=chrome&ie=UTF-8',
        'GSW': 'https://www.google.com/search?q=golden+state+latest+game&oq=golden+state+latest+game&aqs=chrome..69i57.4823j0j9&sourceid=chrome&ie=UTF-8',
        'DAL': 'https://www.google.com/search?q=mavericks+latest+game&oq=mavericks+latest+game&aqs=chrome..69i57.5842j0j9&sourceid=chrome&ie=UTF-8',
        'ATL': 'https://www.google.com/search?q=atlanta+hawks+latest+game&safe=strict&ei=Jre_YLDxLsvVgQbMnJSwAw&oq=atlanta+hawks+latest+game&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEYQ_QEyBggAEBYQHjoICC4QkQIQkwI6BQguEJECOggILhCxAxCDAToCCC46CAgAELEDEIMBOgUIABCxAzoLCC4QsQMQxwEQowI6DgguELEDEIMBEJECEJMCOgQIABBDOgQILhBDOgUIABCRAjoHCC4QsQMQQzoOCC4QsQMQxwEQrwEQkQI6BwgAELEDEEM6AggAUNrF-RhY_u_5GGDG8_kYaAFwAngBgAGyA4gB_S2SAQowLjE3LjYuMy4xmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz&ved=0ahUKEwiwnK3D1YjxAhXLasAKHUwOBTYQ4dUDCA4&uact=5',
        'BKN': 'https://www.google.com/search?q=brooklyn+nets+latest+game&safe=strict&hl=en-AE&authuser=0&ei=j4PAYJa8AY-wwbkPjviH4A4&oq=BROO+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeULjpA1iU7gNgtPgDaABwAngAgAG-AYgB-gaSAQMwLjWYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz',
        'BOS': 'https://www.google.com/search?q=boston+celtics+latest+game&safe=strict&hl=en-AE&authuser=0&ei=0oPAYMvbCteW8gL8uo7gBg&oq=boston+cel+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeOggIABAIEAcQHjoCCABQmaIBWLK1AWCXvQFoAnAAeACAAeABiAG-EpIBBjAuMTIuMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz',
        'CHA': 'https://www.google.com/search?q=charlotte+hornets+latest+game&safe=strict&hl=en-AE&authuser=0&ei=64PAYKL-KYuKgAbPv42ADA&oq=char+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMggIABAIEAcQHjIICAAQCBAHEB5QwqgBWM20AWCmvAFoAXACeACAAcMBiAG4CJIBAzAuNpgBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz',
        'CHI': 'https://www.google.com/search?q=chicago+bulls+latest+game&safe=strict&hl=en-AE&authuser=0&ei=BYTAYImPAsbzgAbxt7PYCQ&oq=chica+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjoICAAQCBAHEB5Qxc4BWIHYAWDM4QFoAXACeACAAfYBiAGUC5IBBTAuMy40mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz',
        'CLE': 'https://www.google.com/search?q=cleveland+cavaliers+latest+game&safe=strict&hl=en-AE&authuser=0&ei=I4TAYKK3G4rrgAa_w5TACA&oq=cle+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMggIABAIEAcQHlD0lQFY86MBYM6sAWgBcAJ4AIABuAGIAeMGkgEDMC41mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz',
        'DEN': 'https://www.google.com/search?q=denver+nuggets+latest+game&safe=strict&hl=en-AE&authuser=0&ei=OoTAYLDBOpTA8gLQ2ZCQAg&oq=den+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeOggIABAIEAcQHlCEeVjfggFgqo8BaAFwAngAgAHeAYgB2geSAQUwLjMuMpgBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz',
        'DET': 'https://www.google.com/search?q=detroit+pistons+latest+game&safe=strict&hl=en-AE&authuser=0&ei=ToTAYP2wKYyUgAbrua_YAg&oq=detro+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeUJmPAVihlAFg8Z0BaABwAngAgAHNAYgB4QiSAQUwLjUuMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz',
        'HOU': 'https://www.google.com/search?q=houston+rockets+latest+game&safe=strict&hl=en-AE&authuser=0&ei=ZITAYJu5C4WhgQa72ZSABA&oq=houston+rocke+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMgYIABAHEB46CAgAEAcQChAeULRwWKF-YN-JAWgAcAJ4AIABkQKIAcEVkgEFMC45LjWYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz',
        'IND': 'https://www.google.com/search?q=indiana+pacers+latest+game&safe=strict&hl=en-AE&authuser=0&ei=d4TAYOmmAYiagAbQ0YGwAQ&oq=indiana+pac+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeOggIABAIEAcQHjoECAAQHjoGCAAQCBAeUJB4WLuHAWCZjwFoAHACeACAAdoBiAGqEZIBBjAuMTAuMpgBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz',
        'LAC': 'https://www.google.com/search?q=los+angeles+clippers+latest+game&safe=strict&hl=en-AE&authuser=0&ei=ioTAYIP2J8vKgQbJ45nYBQ&oq=los+angeles+clippers+latest+game&gs_lcp=Cgdnd3Mtd2l6EAM6BggAEAcQHjoICAAQBxAKEB46CggAEAgQBxAKEB46CAgAEAgQBxAeOgQIIRAKULeMAViNtQFg-LkBaABwAngAgAHOAYgBpR2SAQYwLjIwLjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz&ved=0ahUKEwiD47KzmYrxAhVLZcAKHclxBlsQ4dUDCA4&uact=5',
        'MEM': 'https://www.google.com/search?q=memphis+grizzlies+latest+game&safe=strict&hl=en-AE&authuser=0&ei=o4TAYLG9N4v5gQaNqYfoBQ&oq=memp+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMgYIABAHEB46CAgAEA0QBRAeUK-dAVimogFgnK0BaABwAngAgAGwAogBtQiSAQcwLjMuMS4xmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz',
        'MIA': 'https://www.google.com/search?q=miami+heat+latest+game&safe=strict&hl=en-AE&authuser=0&ei=u4TAYKyEFOLC8gKI5ZSgAg&oq=miami+hear+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIECAAQDTIECAAQDTIGCAAQDRAeOgYIABAHEB46AggAUIZnWItyYN55aABwAngAgAGPAogBsxGSAQUwLjguM5gBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz',
        'MIL': 'https://www.google.com/search?q=milwaukee+bucks+latest+game&safe=strict&hl=en-AE&authuser=0&ei=zITAYK_HA8rrgAbJ6qCQAg&oq=mil+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMgYIABAHEB4yCAgAEAgQBxAeMggIABAIEAcQHjIICAAQCBAHEB4yCAgAEAgQBxAeMggIABAIEAcQHjIICAAQCBAHEB4yCAgAEAcQBRAeMggIABAHEAUQHlDhaliLfmD_hAFoAXACeACAAewBiAGeB5IBBTAuNC4xmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz',
        'MIN': 'https://www.google.com/search?q=timberwolves+latest+game&safe=strict&hl=en-AE&authuser=0&ei=3oTAYOv6Ga-NhbIPwN-fqA4&oq=tim+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMgoIABAIEAcQChAeMggIABAIEAcQHjoECAAQQ1D7vwFYgqICYMOsAmgYcAJ4AIABqQKIAcMgkgEGMC4xOS4zmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz',
        'NOP': 'https://www.google.com/search?q=new+orleans+pelicans+latest+game&safe=strict&hl=en-AE&authuser=0&ei=BoXAYMswl4qFsg_2tZegBg&oq=new+or+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeOgcIABBHELADOgIIAFC9jgJYhpMCYOWcAmgBcAJ4AIABlAKIAacLkgEFMC41LjKYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz',
        'NYK': 'https://www.google.com/search?q=new+york+knicks+latest+game&safe=strict&hl=en-AE&authuser=0&ei=K4XAYOuYJIqMgAbt4bKIDQ&oq=new++latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgIIADICCAAyAggAMgIIADICCAAyAggAUMd3WIR9YIKGAWgAcAJ4AIAB0AGIAfoGkgEFMC40LjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz',
        'OKC': 'https://www.google.com/search?q=oklahoma+city+thunder+latest+game&safe=strict&hl=en-AE&authuser=0&ei=PYXAYNi0NYSMhbIPhOOS8Ak&oq=oklahoma+city+thunder+latest+game&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEA0yCAgAEAgQDRAeOgYIABAHEB46BAghEApQ2lRYrX1g0H5oAHACeACAAb0BiAGNHZIBBDAuMjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz&ved=0ahUKEwiYx-2ImorxAhUERkEAHYSxBJ4Q4dUDCA4&uact=5',
        'ORL': 'https://www.google.com/search?q=orlando+magic++latest+game&safe=strict&hl=en-AE&authuser=0&ei=YoXAYK2rEYiigAba74J4&oq=orlando+magic++latest+game&gs_lcp=Cgdnd3Mtd2l6EAMyAggAOgcIABBHELADUKsPWJwaYKkgaAFwAngAgAG8AYgBigSSAQMwLjOYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwit5JuamorxAhUIEcAKHdq3AA8Q4dUDCA4&uact=5',
        'PHI': 'https://www.google.com/search?q=philadelphia+76ers+latest+game&safe=strict&hl=en-AE&authuser=0&ei=Z4XAYKTnL8Ox8gL4zI5A&oq=phila++latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYATIGCAAQBxAeMgYIABAHEB46BAgAEEM6BQgAEJECOggIABAIEAcQHlCmrAFYrr0BYM3IAWgAcAJ4AIAB8wGIAesLkgEFMC42LjKYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz',
        'PHX': 'https://www.google.com/search?q=phoenix+suns+latest+game&safe=strict&hl=en-AE&authuser=0&ei=goXAYObNMISL8gLK-Zz4Ag&oq=phoen+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYATIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIICAAQCBAHEB4yBggAEA0QHjIICAAQCBANEB4yCAgAEAgQDRAeMggIABAIEA0QHjIICAAQCBANEB4yCAgAEAgQDRAeOgQIABBDOgUIABCRAjoICAAQDRAFEB5QqHFYqoABYO6GAWgAcAJ4AIAB5wGIAb8KkgEFMC42LjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz',
        'POR': 'https://www.google.com/search?q=portland+trail+blazers+latest+game&safe=strict&hl=en-AE&authuser=0&ei=lYXAYI-iG--BhbIP5LKo-AQ&oq=portlan+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYATIGCAAQBxAeMgYIABAHEB46CAgAEAgQDRAeUM98WO-FAWCrjQFoAHACeACAAeEBiAGBDJIBBTAuNi4ymAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz',
        'SAC': 'https://www.google.com/search?q=sacramento+kings+latest+game&safe=strict&hl=en-AE&authuser=0&ei=qIXAYKLINIuNhbIPjqWUgAU&oq=sacr+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeULFzWMaJAWCPkgFoAnACeACAAeoBiAGcCpIBBTAuNi4xmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz',
        'SAS': 'https://www.google.com/search?q=san+antonio+spurs+latest+game&safe=strict&hl=en-AE&authuser=0&ei=vIXAYMHzMLPB8gLLv6rIBA&oq=san+ant+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeOggIABAIEAcQHjoICAAQBxAFEB46BggAEAgQHlDmgAFYm5QBYOGcAWgCcAJ4AIAB3QGIAasRkgEFMC45LjOYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz',
        'TOR': 'https://www.google.com/search?q=toronto+raptors+latest+game&safe=strict&hl=en-AE&authuser=0&ei=0oXAYICKDauKhbIPzfqpuAI&oq=toro+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMgYIABAHEB5Q9n5YxIIBYI-NAWgAcAJ4AIABwwGIAZcHkgEDMC41mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz',
        'UTA': 'https://www.google.com/search?q=utah+jazz+latest+game&safe=strict&hl=en-AE&authuser=0&ei=5YXAYPL-F5KigAbiiJrAAQ&oq=uta+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjoICAAQCBAHEB46CAgAEAcQBRAeUPFcWJlgYO5qaABwAngAgAHOAYgB6wWSAQUwLjMuMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz',
        'WAS': 'https://www.google.com/search?q=washington+wizards+latest+game&safe=strict&hl=en-AE&authuser=0&ei=9IXAYO63FInIgQaOsInQAQ&oq=wash+latest+game&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQBxAeUP1rWJNzYO19aABwAngAgAHCAYgB_AaSAQMwLjWYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz'
    }
    
    
    teem = switcher.get(team,'Invalid')
    try:
        #Getting the appropraite URL from the switch statements and storing that page in a variable
        page = requests.get(teem, headers=headers)
        #Using beautiful soup to parse content on the page
        soup = BeautifulSoup(page.content, 'html5lib')
        #Narrowing down the content to only one class and retrieving the text
        score = soup.find(class_="imso_mh__wl imso-ani imso_mh__tas").get_text()
        #Translating retrieved score from Arabic to English
        return translator.translate(score.strip(), dest="en").text
    except Exception as e:
        return 'ERROR: INVALID ENDPOINT'
    






