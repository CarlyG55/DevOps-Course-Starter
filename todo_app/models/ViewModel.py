class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def to_do_items(self):
        return list(filter(lambda item: item.status == 'To Do', self.items))

    @property
    def doing_items(self):
        return list(filter(lambda item: item.status == 'Doing', self.items))

    @property
    def done_items(self):
        return list(filter(lambda item: item.status == 'Done', self.items))