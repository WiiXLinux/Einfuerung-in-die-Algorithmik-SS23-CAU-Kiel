import copy


class Stack:
    """
    Class describing a Stack.
    """
    def __init__(self):
        """
        Creates an empty Stack.
        An empty Stack doesn't have a left neighbor, and it's Top of Stack is empty.
        A list representing the same idea would be: [], as you can see there isn't any ToS or neighbor.
        """
        self.left = None
        self.tos = None

    def push(self, obj):
        """
        Pushes an object on to the Stack.
        The new tos will have to be adjusted.
        Because we still need the old Stack, we store the old Stack as the Stack left to the ToS.
        :param obj: Object to be pushed on the Stack
        :return:
        """
        self.left = copy.copy(self)
        self.tos = obj

    def top(self):
        """
        Simple getter for the Top element.
        :return: Top of Stack
        """
        return self.tos

    def pop(self):
        """
        Returns the Top of Stack and removes it from the Stack.
        :return: Top of Stack
        """
        # Detects that the current Stack is empty because it's the same as the initialised Stack.
        if self.left is None:
            # Notify the user
            raise Exception("Stack Empty")

        # Because the top of Stack can be anything we'll copy it, because it could be an object that isn't a basic type.
        old_tos = copy.copy(self.tos)
        # The left half is definitely a Stack, so we have to copy it.
        old_left = copy.copy(self.left)

        # Here we don't have to copy since we're not using the original Stack anymore.
        self.left = self.left.left
        # If we didn't have copied the old left and just used self.left.tos, then we would be using the ToS one layer
        # too deep, which would remove one element of the Stack.
        self.tos = old_left.tos

        return old_tos

    def __str__(self):
        """
        Not required for the assigment, but useful to debug the code.
        Converts the Stack into a list and then converts this list into a string.
        We reversed the list because then we can read the right element as ToS.
        :return: String representation of the Stack.
        """
        string = []
        looker = copy.copy(self)
        while looker.left is not None:
            string += [looker.tos]
            looker = looker.left
        string.reverse()
        return str(string)


s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.push("E")

print(s.pop())  # -> E
print(s.pop())  # -> D

s.push("F")
s.push("G")

print(s.pop())  # -> G
print(s.pop())  # -> F
print(s.pop())
print(s.pop())
print(s.pop())
# Add another pop to demonstrate what happens when the Stack is empty.
try:
    print(s.pop())
except Exception as exception:
    print(exception)
