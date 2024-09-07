import os
import requests

BDO_URL = "https://api.arsha.io/v2/na/GetWorldMarketList"
CATEGORIES = [25, 30, 35, 40, 45, 50, 65, 70, 75, 80]
RESOURCES_ITEMS_PATH = "./resources/items"

def update_resources_items():
    if os.path.exists(RESOURCES_ITEMS_PATH):
        os.remove(RESOURCES_ITEMS_PATH)

    out_file = open(RESOURCES_ITEMS_PATH, "w")
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
    out_file.close()

if __name__ == "__main__":
    update_resources_items()