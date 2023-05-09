class BinTree():

    def __init__(self,left = None,value = None,right = None):
         '''
         constructs either an empty bintree or a node in a bintree with subtrees
         left and right,
         call: BinTree() for empty BinTree
               BinTree(tl,v,tr) for node
         '''
         if left == None:
             self.empty = True
         else:
             self.empty = False
             self.left = left
             self.value = value
             self.right = right

    def node(left,value,right):
        '''
        statical method to construct a node in the bintree
        '''
        tree = BinTree()
        tree.empty = False
        tree.left = left
        tree.value = value
        tree.right = right
        return tree
        
    def leaf(value):
        '''
        method construction a leaf, which is an abreviation for a node with two
        empty children
        '''
        return BinTree.node(BinTree(),value,BinTree())
        
    def __str__(self):
        '''
        conversion to string
        '''
        if self.empty:
            return '_'
        else:
            return ('(' + str(self.left) + ','
                        + str(self.value) + ','
                        + str(self.right) + ')')
                        
    def arith_exp_to_str(self):
        '''
        nicer representation, where leafs are printes instead of nodes 
        with empty subtrees
        '''
        if self.empty:
            return '_'
        elif self.left.empty and self.right.empty:
            return str(self.value)
        else:
            return ('(' + self.left.arith_exp_to_str() +
                          str(self.value) +
                          self.right.arith_exp_to_str() + ')')
                          
    def __subtree_at(self,path):
        '''
        method for accessing subtree at given position
        not supposed to be used from outside, since subtree is not copied
        internally needed to mutate the subtree
        '''
        tree = self
        while path != '' and not tree.empty:
            if path[0] == 'l':
                tree = tree.left
            elif path[0] == 'r':
                tree = tree.right
            else:
                raise Exception('no valid path: containing \'' + path[0] +'\'')
            path = path[1:]
       
        if path == '':
            return tree
        else:
            return None

    def subtree_at(self,path):
        '''
        method to select a subtree from outside the class
        a copy of the selected subtree is returned
        '''
        subtree = self.__subtree_at(path)
        if subtree == None:
            return None
        else:
            return subtree.copy()
             
    def update_value_at(self,path,value):
        '''
        mehtode to update the value at a given position
        returns old value in case of success and None otherwise
        '''
        subtree = self.__subtree_at(path)
        if subtree != None:
            old_value = subtree.value
            subtree.value = value
            return old_value
        else:
            return None

    def update_tree_at(self,path,tree):
        '''
        methode to update the subtree at a given position
        returns a boolean indicating whether the update was successful
        '''
        subtree = self.__subtree_at(path)
        if subtree != None:
            if tree.empty:
                subtree.empty = True
            else:
                subtree.value = tree.value
                subtree.left = tree.left
                subtree.right = tree.right
                subtree.empty = False
            return True
        else:
            return False

    def copy(self):
        '''
        make a deep copy of the given tree object.
        only subtrees are copied, values are shared
        '''
        if self.empty:
            return BinTree()
        else:
            return BinTree(self.left.copy(), self.value, self.right.copy())

def next_pos(pos):
    '''
    compute next position in bin trees
    the order is as follows:
    '', 'l', 'r', 'll', 'lr', 'rl', 'rr', 'lll', 'llr', ...
    >>> next_pos('llr')
    'lrl'
    >>> next_pos('rrr')
    'llll'
    '''
    new_pos = ''
    for i in range(len(pos)-1,-1,-1):
        if pos[i] == 'r':
            new_pos = 'l' + new_pos
        else: # pos[i] == 'l'
            new_pos = pos[:i] + 'r' + new_pos
            return new_pos
    return new_pos + 'l'


def prev_pos(path):
    '''
    compute the previous position of a binary tree
    '''
    pass


def positions(bin_tree):
    '''
    computes all positions in a given bin tree
    and returns them as a list
    '''
    #if the tree is empty, return an empty list
    if bin_tree.empty:
        return []
    
    #if there are elements in the bintree, call
    #positions() recursively to get all positions
    else:
        #from the (current) root element go down the left side first
        #for each element that was found in the left side branch
        #call positions() again
        left_pos = [pos + 'l' for pos in positions(bin_tree.left)]

        #then go down the right side of the tree
        right_pos = [pos + 'r' for pos in positions(bin_tree.right)]

        #return all positions that are temporarily stored
        #within left_pos list and right_pos list
        return [''] + left_pos + right_pos

tree = BinTree()        
pos = ''

for i in range(9):
    tree.update_tree_at(pos,BinTree.leaf(i))
    pos = next_pos(pos)


print(prev_pos('lll'))
#print(positions(tree))
#print(tree.arith_exp_to_str())