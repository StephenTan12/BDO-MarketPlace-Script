import logging

from .script import run_script
from .update_resources import update_resources_items

def init():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    update_resources_items()
    run_script()