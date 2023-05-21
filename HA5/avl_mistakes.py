import random
import sys


class SearchTree:
    '''
    Class implementing search trees, with balancing ;)
    '''

    def __init__(self):
        '''
        construct an empty search tree
        '''
        self.empty = True
        self.height = 0
        self.bal = 0

    def _update_height(self):
        '''
        auxiliary function for updating the height of a node.
        '''
        self.height = max(self.left.height, self.right.height) + 1

    def _update_bal(self):
        '''
        auxiliary function for updating the height of a node.
        '''
        self.bal = self.right.height - self.left.height

    def insert(self, v):
        '''
        inserts the given value v into the searchtree
        returns False, if value already occurs, otherwise True 
        '''

        print("Value that should be inserted: " + str(v) + "\nCurrent subtree: " + str(self))

        if self.empty:
            self.value = v
            self.left = SearchTree()
            self.right = SearchTree()
            self.empty = False
            self.height = 1
            # self.bal stays 0
            return True
        elif v == self.value:
            return False
        elif v < self.value:
            result = self.left.insert(v)
            self._rotate()
            return result
        else:
            result = self.right.insert(v)
            self._rotate()
            return result

    def _rotate(self):
        self._update_height()
        self._update_bal()
        if self.bal == 2:
            x = self.value
            y = self.right.value
            if self.right.bal == -1:  # RL-rotation
                print("Führe RL-Rotation durch")
                z = self.right.left.value
                t1 = self.left
                t2 = self.right.left.left
                t3 = self.right.left.right
                t4 = self.right.right
                self.value = z
                self.left = SearchTree()
                self.left.empty = False
                self.left.value = x
                self.left.left = t1
                self.left.right = t2
                self.right = SearchTree()
                self.right.empty = False
                self.right.value = y
                self.right.left = t3
                self.right.right = t4
                self.left._update_height()
                self.right._update_height()
                self.left._update_bal()
                self.right._update_bal()
                self._update_bal()
            else:  # L-rotation
                print("Führe L-Rotation durch")
                t1 = self.left
                t2 = self.right.left
                t3 = self.right.right
                self.value = y
                self.left = SearchTree()
                self.left.empty = False  # hier war Fehler in Vorlesung
                self.left.value = x  # hatten wir vergessen
                self.left.left = t1
                self.left.right = t2
                self.right = t3
                self.left._update_bal()  # should be 0
                self.left._update_height()
                self._update_height()
                self._update_bal()  # should be 0
        elif self.bal == -2:
            x = self.value
            y = self.left.value  # HIER wurde nicht der Wert, sondern ein Baum kopiert, was falsch ist.
            if self.left.bal == 1:  # LR-rotation
                print("Führe LR-Rotation durch")
                z = self.left.right.value
                t1 = self.left.left
                t2 = self.left.right.left
                t3 = self.left.right.right
                t4 = self.right
                self.value = z
                self.left.value = y
                self.left.left = t1
                self.left.right = t2
                self.right = SearchTree()
                self.right.empty = False
                self.right.value = x
                self.right.right = t3
                self.right.left = t4
                self.left._update_height()
                self.right._update_height()
                self.left._update_bal()
                self.right._update_bal()
                self._update_bal()
            else:  # R-rotation
                print("Führe R-Rotation durch")
                t1 = self.left.left
                t2 = self.left.right
                t3 = self.right
                self.value = y
                self.left = t1
                self.right = SearchTree()
                self.left = t1
                self.right.empty = False
                self.right.value = x
                self.right.left = t2
                self.right.right = t3
                self.right._update_height()
                self._update_height()
                self.right._update_bal()  # should be 0
                self._update_bal()  # should be 0

    def elem(self, v):
        '''
        checks whether v occurs in th search tree
        '''
        if self.empty:
            return False
        elif v == self.value:
            return True
        elif v < self.value:
            return self.left.elem(v)
        else:
            return self.right.elem(v)

    def elem_iter(self, v):
        '''
        iterative version of elem
        '''
        st = self
        while not st.empty and v != st.value:
            if v < st.value:
                st = st.left
            else:
                st = st.right
        return not st.empty

    def __str__(self):
        '''
        nice string representation of a search tree, mainly usefull for
        debugging'''
        if self.empty:
            return '_'
        elif self.left.empty and self.right.empty:
            return str(self.value)
        else:
            return ('(' + str(self.left) + ',' + str(self.value) +
                    '[' + str(self.height) + ',' + str(self.bal) + ']' +
                    ',' + str(self.right) + ')')


def rand_list(n, seed=None):
    if seed is None:
        seed = random.randrange(sys.maxsize)
    r = random.Random(seed)
    print("Random seed is: "+str(seed))
    res = []
    for i in range(n):
        res.append(r.randint(1, n * 10))
    print("List is "+str(res))
    return res


l = list(range(10))
n = 4


l = rand_list(n)
st = SearchTree()
for x in l:
    st.insert(x)
    print(st)

print(st.height)

"""
Es gab genau einen Fehler, der zur falschen Semantik und meistens auch zu einem Absturz einer Art
(zu tiefe Rekursionsebene, Typ-Fehler bei einer Komparisation zwischen int und SearchTree) führte:
In (nun) Zeile 104, wo statt y = self.left.value, y = self.left stand, was inkorrekt ist, denn y soll nicht linker
Unterbaum sein, sondern dessen Wert, um den neuen Baum so umzusortieren, dass kein alter Wert verloren geht.

Wir haben noch ein paar prints hinzugefügt, um die Methoden besser verstehen zu können. Dazu haben wir zum Debuggen auch
rand_list so modifiziert, dass wir den Seed selber setzen konnten und, dass dieser auch noch ausgegeben wird.
"""

