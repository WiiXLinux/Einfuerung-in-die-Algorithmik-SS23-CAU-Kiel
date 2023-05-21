import random

class ST():
    '''
    immutable implementation of searchtrees
    every method generates a new searchtree with sharing
    searchtrees cannot be mutated
    '''
    def __init__(self):
        '''
        construct an empty immutable searchtree
        '''
        self.empty = True
    
    def __node(l,v,r):
        '''
        static method as second constructor to construct a
        non-empty node, parameters are left end right tree and value
        '''
        new_node = ST()
        new_node.empty = False
        new_node.left = l
        new_node.value = v
        new_node.right = r
        return new_node
    
    def insert(self,v):
        '''
        return a stack in which the new value is inserted
        '''
        if self.empty:
            return ST.__node(ST(),v,ST())
            # auch möglich:
            # empty = ST()
            # return ST.__node(empty,v,empty)
            # it would even be possible to construct only one
            # single empty node, which is shared all over the
            # tree for empty leaf.
        elif v == self.value:
            return self
        elif v < self.value:
            return ST.__node(self.left.insert(v),self.value,self.right)
        else:
            return ST.__node(self.left,self.value,self.right.insert(v))
        
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

    def __str__(self):
        '''
        nice string representation of a search tree,
        mainly usefull for debugging'''
        if self.empty:
            return '_'
        elif self.left.empty and self.right.empty:
            return str(self.value)
        else:
            return ('(' + str(self.left) + ',' + str(self.value) +
                    ',' + str(self.right) + ')')

    def minvalue(tree):
        '''
        helper function for delete(), returns minimum value in a given
        SearchTree
        '''
        current = tree
        while not current.left.empty:
            current = current.left

        return current.value

    def delete(self,v):
        '''
        method to delete an entry from a search tree
        '''
        if self.value == v:
            #value found, now to deletion

            #case 1: value is at the end of SearchTree (has no child nodes)
            if self.left.empty and self.right.empty:
                self. value = self.__init__()
                self.empty = True

            #case 2: value has one left child an no right child
            elif self.right.empty and not self.left.empty:
                self.value = self.left.value
                self.left.empty = True

            #case 3: value has one right child and no left child
            elif self.left.empty and not self.right.empty:
                self.value = self.right.value
                self.right.empty = True

            #case 4: Value has both left and right children
            elif not self.left.empty and not self.right.empty:
                #replace value with the minimum value in right subtree and
                #delete that node
                temp = self.right.minvalue()
                print(temp)
                self.value = temp
                self.right.delete(temp)

        #if value is smaller/larger than the currently looked at
        #value, continue search on  the left/right branch of SearchTree
        #by recursively calling delete(v)
        elif v < self.value:
            return self.left.delete(v)
        elif v > self.value:
            return self.right.delete(v)

def rand_list(n):
    res = []
    for i in range(n):
        res.append(random.randint(1,n*10))
    return res

#l = [4,7,2,9,8,1,3,2]
n = 10

'''l = rand_list(n)
l[5] = 10
st = ST()
for x in l:
    st = st.insert(x)
    if x == 10:
        st10 = st
    #print(st)'''

st = ST()
st = st.insert(5)
st = st.insert(3)
st = st.insert(7)
st = st.insert(11)
st = st.insert(6)
print(st)

st.delete(5)

print(st)