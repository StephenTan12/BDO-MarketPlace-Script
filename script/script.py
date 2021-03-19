from pymongo import MongoClient
from .scrapper import getItemName
from data import food
import os
import urllib
import requests

body_data = {
  'keyType': 0,
  'mainCategory': 35,
  'subCategory': 4
}

def run_script():
  
  print('hello')
  user = os.getenv('MONGO_USER')
  password = os.getenv('MONGO_PASS')
  password = urllib.parse.quote(password)
  client = MongoClient(f'mongodb+srv://{user}:{password}@marketdata.2lgr9.mongodb.net/food?retryWrites=true&w=majority')

  response = requests.post(
    'https://na-trade.naeu.playblackdesert.com/Trademarket/GetWorldMarketList',
    params=body_data,
    headers={'Content-Type': 'application/json', 'User-Agent': 'BlackDesert'},
  )
  res_data = response.json()

  database_food = client['food']

  items_data = res_data['resultMsg'].split('|')

  for i in items_data:
    item = i.split('-')
    try:
      itemId = int(item[0])
      currentStock = int(item[1])
      totalTrades = int(item[2])
      price = int(item[3])

      item_name = ''

      if food.has_key(itemId):
        item_name = food[itemId]
      else:
        item_name = getItemName(itemId)
        food[itemId] = item_name

      col_item = database_food[item_name]

      document = {
        'itemId': itemId,
        'currentStock': currentStock,
        'totalTrades': totalTrades,
        'price': price
      }

      col_item.insert_one(document)
    except:
      continue