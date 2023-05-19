# logging
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",filename="log/debugging.log", encoding='utf-8')
logging.info("Start of the program")

# Database

from sqlalchemy import create_engine
import pandas as pd
import json

with open(".secrets.json", "r") as f:
  dict_secrets = json.load(f) #read .secrets.json / this is a setting file
  """
  This is a sample of .secrets.json
    {
    "db": {
      "database": "database name",
      "user": "root",
      "password": "your password",
      "host": "127.0.0.1:3306"
    }
  }
  """

try:
  host = dict_secrets["db"]["host"]
  user = dict_secrets["db"]["user"]
  password = dict_secrets["db"]["password"]
  db = dict_secrets["db"]["database"]
except:
  logging.error("Please check .secrets.json")
  exit(1)

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8')
con = engine.connect()

