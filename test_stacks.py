from stacks import Stack, StackOverflowError, StackUnderflowError, StackInvalidCapacity


# capacity
# len()
# is_empty()
# push(value)
# pop()
# peek()
# find()

def test_empty_stack():
    stack = Stack(10)
    assert stack.is_empty()


def test_len():
    stack = Stack(10, [1, 2, 3, 4, 5])
    assert stack.stack_len() == 5


def test_push():
    push_value = 17
    stack = Stack(10, 1)
    temp_list = stack.push(push_value)
    print(temp_list)
    assert temp_list[1] == push_value

def test_peek():
    a_test_list = [1,2,3,4,5,6]
    stack = Stack(10, a_test_list)
    assert stack.peek() == a_test_list[-1]

def test_capacity():
    stack = Stack(5, [1,2,3,4,5])
    assert stack.init_capacity(5, [1,2,3,4,5]) == True

def test_capacity_stack_overflow():
    try:
        stack = Stack(4, [1, 2, 3, 4, 5])
        assert False
    except StackOverflowError:
        assert True

def test_pop():
    stack = Stack(5, [1,2,3,4,5])
    assert stack.pop() == 5

