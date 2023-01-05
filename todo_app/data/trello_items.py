import os
import requests
from itertools import chain
from todo_app.models.Item import Item


board_id = os.getenv('BOARD_ID')
api_key = os.getenv("API_KEY")
token = os.getenv("TOKEN")
base_url = f'https://api.trello.com/1'
base_query_params = {
    'key': api_key,
    'token': token,
    'cards': 'open',
}
list_url = f'{base_url}/boards/{board_id}/lists'
base_query_string = f'?key={api_key}&token={token}&cards=open'

def get_cards():
  lists = requests.get(f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}/lists?key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}&cards=open').json()
  nested_cards = [[Item.from_trello_card(card, list) for card in list['cards']] for list in lists]
  return list(chain.from_iterable(nested_cards))

def add_card(card_name):
  requests.post(f'https://api.trello.com/1/cards?key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}&cards=open&name={card_name}&idList={os.getenv("TO_DO_LIST_ID")}')

def move_card_to_list(card_id, list_id):
  requests.put(f'https://api.trello.com/1/cards/{card_id}/?key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}&cards=open&idList={list_id}')