import requests
import sys
from time import sleep
from tabulate import tabulate


def get_scams(api_key):
    scams = []
    headers = {"x-api-key": api_key}
    r = requests.get('https://tarkov-market.com/api/v1/items/all', headers=headers)
    for i in r.json():
        r2 = requests.get('https://tarkov-market.com/api/v1/item?uid='+i['uid'], headers=headers)
        while r2.status_code == 429:
            print("Got rate limited, sleeping")
            sleep(15)
            r2 = requests.get('https://tarkov-market.com/api/v1/item?uid=' + i['uid'], headers=headers)
        data = r2.json()[0]
        if data['traderPrice'] > data["price"]:
            scams.append([i['name'], data['price'], data['traderName'], data['traderPrice']-data['price']])
    scams.sort(key=lambda x: x[3])
    print(tabulate(scams, headers=["Item", "Market Price", "Trader", "Profit"]))


if __name__=='__main__':
    try: 
        with open('.secret', 'r') as f:
            secret = f.read().strip()
    except IOException:
        secret = sys.argv[1]
    get_scams(secret)
