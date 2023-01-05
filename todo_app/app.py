from flask import Flask, redirect, render_template, request
from itertools import chain
from todo_app.flask_config import Config
from todo_app.Item import Item
import os
import requests

app = Flask(__name__)
app.config.from_object(Config())

board_id = os.getenv('BOARD_ID')
api_key = os.getenv('API_KEY')
token = os.getenv('TOKEN')
base_url = f'https://api.trello.com/1'
base_query_params = {
    'key': api_key,
    'token': token,
    'cards': 'open',
}
list_url = f'{base_url}/boards/{board_id}/lists'
list_query_params = query_params = dict(base_query_params, **{'cards': 'open'})

@app.route('/')
def index():
    lists = requests.get(list_url, list_query_params).json()
    nested_cards = [[Item.from_trello_card(card, list) for card in list['cards']] for list in lists]
    cards = list(chain.from_iterable(nested_cards))
    return render_template('index.html', cards = cards)


@app.route('/submit', methods=["POST"])
def submit_form():
    url = f'{base_url}/cards'
    query_params = dict(base_query_params, **{'name': request.form.get('title'), 'idList': os.getenv('TO_DO_LIST_ID')})
    requests.post(url, query_params)
    return redirect('/')

@app.route('/update-status/<card_id>/<current_list>', methods=["POST"])
def update_status(card_id, current_list):
    url = f'{base_url}/cards/{card_id}'
    if current_list == 'To Do':
        query_params = dict(base_query_params, **{'idList': os.getenv('DOING_LIST_ID')})
        requests.put(url, query_params)
    if current_list == 'Doing':
        query_params = dict(base_query_params, **{'idList': os.getenv('DONE_LIST_ID')})
        requests.put(url, query_params)

    return redirect('/')
