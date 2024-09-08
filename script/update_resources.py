import os
import requests
import logging
import datetime

BDO_URL = "https://api.arsha.io/v2/na/GetWorldMarketList"
CATEGORIES = [25, 30, 35, 40, 45, 50, 65, 70, 75, 80]
RESOURCES_ITEMS_PATH = "./resources/items"

def update_resources_items():
    if not os.path.exists(RESOURCES_ITEMS_PATH):
        _update()
    elif datetime.datetime.now().weekday() == 3: # check if thursday
        if os.path.exists(RESOURCES_ITEMS_PATH):
            os.remove(RESOURCES_ITEMS_PATH)
        _update()

def _update():
    out_file = open(RESOURCES_ITEMS_PATH, "w")
    
    logging.info("Fetching item ids")
    for category in CATEGORIES:
        response = requests.get(
            url=BDO_URL,
            params={"mainCategory": category}
        )

        response_json = response.json()

        for item in response_json:
            item_id = item["id"]
            item_main_category = item["mainCategory"]
            item_sub_category = item["subCategory"]
            out_file.write(f"{item_id} {item_main_category} {item_sub_category}\n")
    
    logging.info("Done fetching item ids")
    out_file.close()