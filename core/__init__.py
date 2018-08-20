import sys
import os
from json import loads

# Get current dir
dirname = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dirname, 'windows'))

# from core import MacronCoreAPI
from window import create_window

def get_os():
  return

def main(args):
  app_config = loads(loads(args[1]))
  # app_root_path = app_config["appRootPath"].replace("//", "\u005c")
  # app_html_path = app_config["sourcePath"]
  # app_dev_uri = app_config["devServerURI"]
  
  # @todo handle err
  if "mainWindow" not in app_config:
    print("Error: 'mainWindow' property not defined in macron.config.js")

  create_window(config=app_config["mainWindow"])

if __name__ == "__main__":
  main(args=sys.argv)
