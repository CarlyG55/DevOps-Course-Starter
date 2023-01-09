from flask import Flask, redirect, render_template, request
from todo_app.flask_config import Config
from todo_app.models.ViewModel import ViewModel
from todo_app.data.trello_items import get_cards, add_card, move_card_to_list
import os

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        cards_view_model = ViewModel(get_cards())
        return render_template('index.html', view_model = cards_view_model)


    @app.route('/submit', methods=["POST"])
    def submit_form():
        name = request.form.get('title')
        add_card(name)
        return redirect('/')

    @app.route('/update-status/<card_id>/<current_list>', methods=["POST"])
    def update_status(card_id, current_list):
        if current_list == 'To Do':
            move_card_to_list(card_id, os.getenv('DOING_LIST_ID'))
        if current_list == 'Doing':
            move_card_to_list(card_id, os.getenv('DONE_LIST_ID'))
        return redirect('/')
    
    return app
