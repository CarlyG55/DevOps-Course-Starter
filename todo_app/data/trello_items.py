import os
import requests
from itertools import chain
from todo_app.models.Item import Item

def get_cards():
  lists = requests.get(f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}/lists?key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}&cards=open').json()
  nested_cards = [[Item.from_trello_card(card, list) for card in list['cards']] for list in lists]
  return list(chain.from_iterable(nested_cards))

def add_card(card_name):
  requests.post(f'https://api.trello.com/1/cards?key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}&cards=open&name={card_name}&idList={os.getenv("TO_DO_LIST_ID")}')

def move_card_to_list(card_id, list_id):
  requests.put(f'https://api.trello.com/1/cards/{card_id}/?key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}&cards=open&idList={list_id}')