import requests
from datetime import datetime

def get_tuntihinta():
    url = 'https://api.porssisahko.net/v1/price.json?'
    pvm = datetime.now()
    parametrit = 'date='+ str(pvm.strftime("%Y-%m-%d")) + "&hour=" + str(pvm.strftime("%H"))
    url += parametrit

    try:
        response = requests.get(url)
        if response.status_code == 200:
            tuntihinta = response.json()
            print(f'Tuntihinta nyt {tuntihinta["price"]} snt/kWh')
        else:
            print('Error:', response.status_code)
            return None
    except:
        return None

if __name__ == "__main__":
    get_tuntihinta()