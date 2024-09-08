import logging
import time
import traceback

from .update_resources import RESOURCES_ITEMS_PATH
from .api import fetch_bdo_market_data
from .models import get_item_data
from .cloud_sql_db_conn import insert_to_database

def run_script():
    resources_items_file = open(RESOURCES_ITEMS_PATH, "r")

    start_time = time.time()
    logging.info("Started fetching item data")
    for line in resources_items_file:
        (item_id, main_category_id, sub_category_id) = line.strip().split(" ")

        logging.info("Requesting item id %s", item_id)
        request_params = _create_request_params(item_id)
        items_json_response = fetch_bdo_market_data(request_params)

        try:
            logging.info("Formatting response for item id %s", item_id)
            item_data = get_item_data(items_json_response, main_category_id, sub_category_id)

            logging.info("Inserting item id %s into cloud sql", item_id)
            insert_to_database(item_data)
        except Exception as e:
            logging.error("Error occurred at item id %s: %s", item_id, e)
            logging.error("stack trace: %s", traceback.format_exc())

    logging.info("Total time taken for request and insertion is %s seconds", (time.time() - start_time))
    resources_items_file.close()

def _create_request_params(item_id: str) -> dict[str]:
    return {"id": int(item_id), "lang": "en"}