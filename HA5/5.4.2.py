'''
The time complexity of the copy method is O(n), with n being the
total number of nodes within a given SearchTree. When calling copy()
every node of the original tree is "looked at" exactly once, and then
directly copied into the newTree. Within copy() the methods insert() and
_update_height() are being called as well, both having a time complexity
of O(1), since both are only handling one node for each call.

The absence of a copy operation in an immutable implementation of a search
tree is because the original tree is never modified. If a new node is
inserted into the tree or a node is deleted, a new tree is created with
the required changes, while the original tree remains unchanged. This
approach eliminates the need for copying nodes. In contrast, a mutable
implementation of a search tree modifies the structure and values of nodes
directly. If a new node is inserted into a mutable search tree, the
existing nodes are modified, changing their pointers and updating their
values. This mutability necessitates the use of copy operations to preserve
the integrity of the original tree and its associated data while performing
modifications.
'''

import random

class SearchTree():

    '''
    Class implementing search trees, without balancing
    '''

    def __init__(self):
        '''
        construct an empty search tree
        '''
        self.empty = True
        self.height = 0

    def copy(self):
        '''
        method to copy a given searchtree
        '''
        newTree = SearchTree()

        if self.empty:
            return newTree

        #insert current value into newTree; because the function calls
        #itself recursively, no further specifications about the placement
        #of the current node need to be made.
        newTree.insert(self.value)

        #recursively call copy() to copy each branch of the SearchTree
        newTree.left = self.left.copy()
        newTree.right = self.right.copy()

        newTree._update_height()
        return newTree

    def _update_height(self):
        '''
        auxiliary function for updating the height of a node.
        '''
        self.height = max(self.left.height, self.right.height) + 1

    def insert(self,v):
        '''
        inserts the given value v into the searchtree
        returns False, if value already occurs, otherwise True
        '''
        if self.empty:
            self.value = v
            self.left = SearchTree()
            self.right = SearchTree()
            self.empty = False
            self.height = 1
            return True
        elif v == self.value:
            return False
        elif v < self.value:
            result = self.left.insert(v)
            self._update_height()
            return result
        else:
            result = self.right.insert(v)
            self._update_height()
            return result

    def elem(self,v):
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
        
    def elem_iter(self,v):
        '''
        iterative version of elem
        '''
        st = self
        while not st.empty and v != st.value:
            if v < self.value:
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
                    '[' + str(self.height) + ']' +
                    ',' + str(self.right) + ')')
                    
        
def rand_list(n):
    res = []
    for i in range(n):
        res.append(random.randint(1,n*10))
    return res

#l = [4,7,2,9,8,1,3,2]
n = 10

l = rand_list(n)
st = SearchTree()
'''for x in l:
    st.insert(x)'''
    #print(st)

st.insert(3)
st.insert(4)
st.insert(9)
st.insert(12)
st.insert(8)
st.insert(0)
st.insert(2)
st.insert(11)
st.insert(5)
st.insert(23)
st.insert(10)
st.insert(13)

print(st)
print(st.copy())