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
    tunti = 0
    pvm = datetime.now().strftime("%Y-%m-%d")
    print(f'Sähkön hinta {datetime.now().strftime("%d.%m.%Y")}')
    print('Tunti   Hinta')
    while tunti < 24:
        tuntihinta = get_tuntihinta(pvm,tunti)
        print(f'{str(tunti).zfill(2)}-{str(tunti+1).zfill(2)}   {round(tuntihinta,2)} snt/kWh')
        tunti += 1

    return None

if __name__ == "__main__":
    get_tuntihintanyt()
    get_paivanhinnat()