'''assignment 2.3: Zeigerstruktur
every node in the structure consists of one value and one pointer
implement as:
nested list (two elements per list) ;;; line 11 - 18
nested dicts ;;; line 24 - 35
objects/class ;;; line 40 - 70
'''

#nested list

l = [42, [73, [55, [42, None]]]]
#p1 points to the item at the far left, p2 points to the item in the right bottom corner
p1 = l[0]
p2 = l[1][1][1][0]

#add python code that changes the 73 to an 42
#access list item 73 
l[1][0] = 42


###################
#nested dict

d = {'value': 42, 'next': {
    'value': 73, 'next': {
        'value': 55, 'next': {
            'value': 42, 'next': None
            }}}}

#p1 and p2 from the graphic are renamed to d1 and d2, so it is easier to differentiate between what variables point to
#what part of the assignment
d1 = d['value']
d2 = d['next']['next']['next']['value']

d['next']['value'] = 42

###################
#objects/class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def set_next(self, other):
        '''set_next is a method to link different nodes to one another'''
        self.next = other
    def change_node(self, newvalue):
        '''change_node is a method to change the value of a node
        >>> n2.change_node(42)
        42'''
        self.value = newvalue
    
#define objects
n1 = Node(42)
n2 = Node(73)
n3 = Node(55)
n4 = Node(42)

#initialize pointers, link nodes
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
n4.set_next(n3)

#as before: variables p1 and p2 are here renamed to c1 and c2, so for each method of implementing the structure
#there are different variables to check if everything works.
c1 = n1.value
c2 = n1.next.next.next.value

n2.change_node(42)
