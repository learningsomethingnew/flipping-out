from InClass import Stack

def test_creating_new_stack_is_empty():
    stack = Stack()
    assert stack.is_empty()

def test_if_new_stack_has_capacity():
    stack = Stack()
    assert stack.has_capacity()

def test_add_to_stack():
    stack = Stack(5)
    stack.push(5)
    assert not stack.is_empty()

