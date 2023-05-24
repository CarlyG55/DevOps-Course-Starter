class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status
    
    @classmethod
    def from_db_card(cls, card):
        return cls(card['_id'], card['name'], card['status'])