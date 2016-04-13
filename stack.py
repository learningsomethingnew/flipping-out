##############################################################
# File last modified on: 04/12/2016
# Generic stacks class that will manage the number of items
# a list can hold. Starts with a capacity of 10.
##############################################################

class Stack():
    def __init__(self, a_capacity=10, a_list=None):
        # checks for incoming types and converts them to be what they need to be.
        # a_list = self.test_type(a_list)

        # Tests to see if list is negative capacity or if list is over the capacity size.
        #  Raises exceptions if found.
        if a_list is None:
            a_list = []
        if self.init_capacity(a_capacity, a_list):
            self.stack_capacity = a_capacity
            self.values = self.test_type(a_list)

    """Returns T/F if the stack is empty or not"""

    def is_empty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def stack_len(self):
        return len(self.values)

    """Pushes a value into the stack if it has capacity"""

    def push(self, a_value):
        if self.capacity_push():
            self.values.append(a_value)
            return self.values


    """Returns the top most value without removing"""

    def peek(self):
        # Checks to see if the capacity rules are still in affect.
        if self.stack_len() != 0:
            peek_value = self.values[-1]
            return peek_value
        else:
            return None

    """Removes the most top item"""

    def pop(self):
        if self.capacity_pop():
            return self.values.pop()

    """Checks to see if the stack is over capacity"""

    def capacity_push(self):
        # test to see if stack is at capacity. Raises exception
        if self.stack_len() >= self.stack_capacity:
            raise StackOverflowError("stack is greater than capacity")
        else:
            return True

    """Checks to see if the stack is empty before a pop"""

    def capacity_pop(self):
        # tests to see if stack is empty before action
        if self.stack_len() == 0:
            raise StackUnderflowError("stack is empty")
        else:
            return True

    def init_capacity(self, a_cap, a_list):
        # test to see if cap is less than one. If so, exception.
        if a_cap < 1:
            raise StackInvalidCapacity("cap value 0 or -number")

        # if the list coming in is greater than the cap, exception
        elif type(a_list) == list and len(a_list) > a_cap:
            raise StackOverflowError("Length of list is greater than capacity")

        # otherwise return true
        else:
            return True

    def test_type(self, a_value):
        if type(a_value) == int or type(a_value) == float:
            return [a_value]
        else:
            return a_value

    def get_capacity(self):
        return self.stack_capacity


"""try push pasts it's capacity"""


class StackOverflowError(Exception):
    pass


"""try pop an empty stack"""


class StackUnderflowError(Exception):
    pass


"""try create a stack with a negative capacity"""


class StackInvalidCapacity(Exception):
    pass


if __name__ == '__main__':
    f = Stack(10, 1)
    f.push(8)
    #########################################################################################
    #                                      Old Code
    #########################################################################################
    # elif type(a_list) == int or type(a_list) == float:
    #     self.values = [a_list]
    #     return True
