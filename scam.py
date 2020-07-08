import requests
import sys


def get_scams(api_key):
    headers = {"x-api-key": api_key}
    r = requests.get('https://tarkov-market.com/api/v1/items/all', headers=headers)
    for i in r.json():
        data = requests.get('https://tarkov-market.com/api/v1/item?uid='+i['uid'], headers=headers).json()[0]
        #if data['traderPrice'] > data["price"] or data['traderPrice'] > data["avg24hPrice"] or data['traderPrice'] > data["avg7daysPrice"]:
        if data['traderPrice'] > data["price"]:
            print("BUY {item} AND SELL TO {merch} FOR {p} PROFIT".format(item=i['name'], merch=data['traderName'], p=data['traderPrice'] - data['price']))


if __name__=='__main__':
    get_scams(sys.argv[1])
        
