from pymongo import MongoClient
from datetime import date
from .scrapper import getItemName
from .api import getMarketData
import os
import urllib

body_data = [
  {
    'keyType': 0,
    'mainCategory': 35,
    'subCategory': 4
  },
  {
    'keyType': 0,
    'mainCategory': 25,
    'subCategory': 3
  }
]

categories = ['food', 'materials']

def run_script():
  user = os.getenv('MONGO_USER')
  password = os.getenv('MONGO_PASS')
  password = urllib.parse.quote(password)

  for (index, category) in enumerate(categories):
    client = MongoClient(f'mongodb+srv://{user}:{password}@marketdata.2lgr9.mongodb.net/{category}?retryWrites=true&w=majority')
    database_collection = client[category]
    items_data = getMarketData(body_data[index])

    for i in items_data:
      item = i.split('-')
      try:
        itemId = int(item[0])
        currentStock = int(item[1])
        totalTrades = int(item[2])
        price = int(item[3])
        date = date.today()

        item_name = getItemName(itemId)

        col_item = database_collection[item_name]

        document = {
          'itemId': itemId,
          'currentStock': currentStock,
          'totalTrades': totalTrades,
          'price': price,
          'date': date
        }

        col_item.insert_one(document)
      except:
        continue