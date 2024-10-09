import requests
from datetime import datetime, timedelta

def get_tuntihintanyt():
    url = 'https://api.porssisahko.net/v1/price.json?'
    pvm = datetime.now()
    parametrit = 'date='+ str(pvm.strftime("%Y-%m-%d")) + "&hour=" + str(pvm.strftime("%H"))
    url += parametrit

    try:
        response = requests.get(url)
        if response.status_code == 200:
            tuntihinta = response.json()
            tuntinyt = pvm.strftime("%H.%M")
            print(f'Tuntihinta nyt (klo {tuntinyt}) on {tuntihinta["price"]} snt/kWh')
        else:
            print('Error:', response.status_code)
            return None
    except:
        return None
    
def get_tuntihinta(pvm: str, tunti: str):
    url = 'https://api.porssisahko.net/v1/price.json?'
    parametrit = 'date='+ str(pvm) + "&hour=" + str(tunti)
    url += parametrit

    tuntihinta = ''
    try:
        response = requests.get(url)
        if response.status_code == 200:
            tuntihinta = response.json()
            return tuntihinta["price"]
            #return print(f'{tuntihinta["price"]} snt/kWh')
        else:
            return None
    except:
        return None

def get_paivanhinnat():
    tuntihinnat = {}
    tunti = 0
    pvm = datetime.now().strftime("%Y-%m-%d")
    
    while tunti < 24:
        tuntihinta = get_tuntihinta(pvm,tunti)
        tuntihinnat[tunti] = tuntihinta
        tunti += 1
    
    print(f'Sähkön hinta {datetime.now().strftime("%d.%m.%Y")}')
    print('Tunti   Hinta (snt/kWh)')
    for tunti, hinta in tuntihinnat.items():
        print(f"{tunti:02d}-{(tunti+1):02d}:   {'%.3f' % hinta}")
    return None

if __name__ == "__main__":
    get_tuntihintanyt()
    get_paivanhinnat()