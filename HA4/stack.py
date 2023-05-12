# Same file used in the lecture. I just fixed some warnings from my ide.
class ListElem:

    def __init__(self):
        self.next = None
        self.value = None
        self.empty = True

    def add(self, v):
        new_head = ListElem()
        new_head.empty = False
        new_head.value = v
        new_head.next = self
        return new_head


class Stack:

    def __init__(self):
        self.st = ListElem()

    def push(self, v):
        self.st = self.st.add(v)

    def top(self):
        if self.st.empty:
            return None
        else:
            return self.st.value

    def pop(self):
        if self.st.empty:
            return None
        else:
            value = self.st.value
            self.st = self.st.next
            return value

    def is_empty(self):
        return self.st.empty

    def __str__(self):
        res = '<-'
        elem = self.st
        while not elem.empty:
            res = res + '<-' + str(elem.value)
            elem = elem.next
        return res
