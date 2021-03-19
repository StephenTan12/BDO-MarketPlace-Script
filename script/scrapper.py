from bs4 import BeautifulSoup
import requests

def getItemName(id):
  url = f'https://bdocodex.com/us/item/{id}/'
  html_text = requests.get(url).text
  soup = BeautifulSoup(html_text, features="html.parser")
  job = soup.find('head')
  item_name = job.find('title').text
  formatted_item_name = item_name[0:item_name.index('-')-1]
  return formatted_item_name