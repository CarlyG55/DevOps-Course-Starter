import pytest
from todo_app.models.Item import Item
from todo_app.models.ViewModel import ViewModel

def test_to_do_items():
    # Arrange
    to_do_item = Item(1, 'Devops month 4', 'To Do')
    doing_item = Item(2, 'Devops month 3', 'Doing')
    done_item = Item(3, 'Devops month 2', 'Done')

    view_model = ViewModel([to_do_item, doing_item, done_item])

    # Act
    to_do_items = view_model.to_do_items

    # Assert
    assert len(to_do_items) == 1
    assert to_do_items[0] == to_do_item

def test_doing_items():
    # Arrange
    to_do_item = Item(1, 'Devops month 4', 'To Do')
    doing_item = Item(2, 'Devops month 3', 'Doing')
    done_item = Item(3, 'Devops month 2', 'Done')

    view_model = ViewModel([to_do_item, doing_item, done_item])

    # Act
    doing_items = view_model.doing_items

    # Assert
    assert len(doing_items) == 1
    assert doing_items[0] == doing_item

def test_done_items():
    # Arrange
    to_do_item = Item(1, 'Devops month 4', 'To Do')
    doing_item = Item(2, 'Devops month 3', 'Doing')
    done_item = Item(3, 'Devops month 2', 'Done')

    view_model = ViewModel([to_do_item, doing_item, done_item])

    # Act
    done_items = view_model.done_items

    # Assert
    assert len(done_items) == 1
    assert done_items[0] == done_item