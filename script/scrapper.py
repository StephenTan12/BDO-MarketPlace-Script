from bs4 import BeautifulSoup
import requests

'''
Scrapper that scraps bdocodex for the item names based on id

@params id - id of the item
@returns the item name corresponding to the id
'''
def getItemName(id):
  url = f'https://bdocodex.com/us/item/{id}/'
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, features="html.parser")
  job = soup.find('head')
  item_name = job.find('title').text
  formatted_item_name = item_name[0:item_name.index('BDO Codex')-3]
  
  return formatted_item_name