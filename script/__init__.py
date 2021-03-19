from .script import run_script
from os.path import dirname
import sys

def init():
  sys.path.append(dirname(__file__))
  run_script()