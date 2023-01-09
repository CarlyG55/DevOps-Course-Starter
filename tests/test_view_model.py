import pytest
from todo_app.models.Item import Item
from todo_app.models.ViewModel import ViewModel

@pytest.fixture
def to_do_item():
    return Item(1, 'Devops month 4', 'To Do')

@pytest.fixture
def doing_item():
    return Item(2, 'Devops month 3', 'Doing')

@pytest.fixture
def done_item():
    return Item(3, 'Devops month 2', 'Done')

@pytest.fixture
def view_model_with_items(to_do_item, doing_item, done_item):
    return ViewModel([to_do_item, doing_item, done_item])

def test_to_do_items(view_model_with_items, to_do_item):
    # Act
    to_do_items = view_model_with_items.to_do_items

    # Assert
    assert len(to_do_items) == 1
    assert to_do_items[0] == to_do_item

def test_doing_items(view_model_with_items, doing_item):
    # Act
    doing_items = view_model_with_items.doing_items

    # Assert
    assert len(doing_items) == 1
    assert doing_items[0] == doing_item

def test_done_items(view_model_with_items, done_item):
    # Act
    done_items = view_model_with_items.done_items

    # Assert
    assert len(done_items) == 1
    assert done_items[0] == done_item