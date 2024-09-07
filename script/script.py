import datetime

from .update_resources import RESOURCES_ITEMS_PATH
from .api import fetch_bdo_market_data

class ItemData:
  def __init__(
      self, date: datetime, id: int, main_category_id: int, sub_category_id: int,
      name: str, base_price: int, 
      current_stock: int, total_trades: int,
      price_min: int, price_max: int, is_patch_day: bool
    ):
    self.date = date
    self.id = id
    self.main_category_id = main_category_id
    self.sub_category_id = sub_category_id
    self.name = name
    self.base_price = base_price
    self.current_stock = current_stock
    self.total_trades = total_trades
    self.price_min = price_min
    self.price_max = price_max
    self.is_patch_day = is_patch_day

  def __str__(self):
    return f"{self.date} {self.id} {self.main_category_id} {self.sub_category_id} {self.name} \
      {self.base_price} {self.current_stock} {self.total_trades} {self.price_min} {self.price_max} {self.is_patch_day}"

def run_script():
  resources_items_file = open(RESOURCES_ITEMS_PATH, "r")

  for line in resources_items_file:
    (item_id, main_category_id, sub_category_id) = line.strip().split(" ")

    request_params = create_request_params(item_id)
    items_json_response = fetch_bdo_market_data(request_params)
    
    item_data = get_item_data(items_json_response, main_category_id, sub_category_id)
    
    # store to database
    
  resources_items_file.close()

def create_request_params(item_id: str) -> dict[str]:
  return {"id": int(item_id), "lang": "en"}

def get_item_data(items_json_response: dict, main_category_id: str, sub_category_id) -> ItemData:
  date = datetime.datetime.now().strftime("%Y-%m-%d")
  id = items_json_response["id"]
  name = items_json_response["name"]
  base_price = items_json_response["basePrice"]
  current_stock = items_json_response["currentStock"]
  total_trades = items_json_response["totalTrades"]
  price_min = items_json_response["priceMin"]
  price_max = items_json_response["priceMax"]
  is_patch_day = datetime.datetime.now().weekday() == 3 # check if Thursday
  
  return ItemData(date, id, main_category_id, sub_category_id, name, base_price, current_stock, total_trades, price_min, price_max, is_patch_day)


