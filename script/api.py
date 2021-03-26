import requests

'''
Does a post request to the Black Desert Online servers to fetch market place data

@params body_data - category id of the items 
@returns list of response data
'''
def getMarketData(body_data):
  response = requests.post(
    'https://na-trade.naeu.playblackdesert.com/Trademarket/GetWorldMarketList',
    params=body_data,
    headers={'Content-Type': 'application/json', 'User-Agent': 'BlackDesert'},
  )
  res_data = response.json()
  items_data = res_data['resultMsg'].split('|')

  return items_data
