import os
from todo_app.models.Item import Item
import pymongo

def get_collection():
  client = pymongo.MongoClient(f'{os.getenv("DB_CONNECTION_STRING")}')
  db = client[f'{os.getenv("DB_NAME")}']
  return db.card

def get_cards():
  collection = get_collection()
  cards = collection.find()
  return [Item.from_db_card(card) for card in cards]

def add_card(card_name):
  collection = get_collection()
  collection.insert_one({"name": card_name, "status": "To Do"})

def change_card_status(card_id, status):
  collection = get_collection()
  collection.update_one({"_id": card_id}, {"$set": {"status": status}})