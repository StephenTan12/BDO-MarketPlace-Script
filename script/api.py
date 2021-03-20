import requests

def getMarketData(body_data):
  response = requests.post(
    'https://na-trade.naeu.playblackdesert.com/Trademarket/GetWorldMarketList',
    params=body_data,
    headers={'Content-Type': 'application/json', 'User-Agent': 'BlackDesert'},
  )
  res_data = response.json()
  items_data = res_data['resultMsg'].split('|')

  return items_data
