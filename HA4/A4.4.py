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

    def delete_largest(self):
        '''
        deletes the largest value from a not empty searchtree
        and returns it
        '''
        st = self
        while not st.empty and not st.right.empty:
            st = st.right
            if st.right == None:
                if st.left.empty:
                    temp = st.value
                    st.value = SearchTree()
                    return temp
                else:
                    templeft = st.left.value
                    temp = st.value
                    st.value = st.insert(templeft)
                    return temp
            if st.right.empty:
                if st.left.empty:
                    temp = st.value
                    st.value = SearchTree()
                    return temp
                else:
                    templeft = st.left.value
                    temp = st.value
                    st.value = st.insert(templeft)
                    return temp

    def delete(self, v):
        '''
        function to delete a value and substitute 
        with the largest value in the left branch

        does not work properly yet, because by 
        calling delete_largest() within delete()
        the return value is always none, so insert can
        not be used to insert the deleted subtree into
        place
        '''
        st = self
        #look for the value similar to the elem function
        #print(v)
        if v == st.value:
            #if found, call delete_largest function for
            #the left subtree of the current node
            #and use returned value to add to current node
            print(st.value)
            if not st.left.empty:
                if st.right.empty:
                    #value of delete largest is not returned 
                    #within the function for a reason I do not
                    #understand whatsoever
                    st.value = st.insert(st.left.delete_largest())
            else:
                if st.left.empty:
                    if st.right.empty:
                        st.left = None
                        st.right = None
                        st.value = None
                        st.empty = True
                    else:
                        # self = self.right
                        st.left = st.right
                        st.right = SearchTree()
            #print(st.delete_largest())
        elif v < st.value:
            st.left.delete(v)
        else:
            st.right.delete(v)

        
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
#print(st.height)
print(st.left.delete_largest())
#print(st.delete(11))
st.delete(11)
print(st)