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
    
    @staticmethod
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
                raise Exception('no valid path: ontaining \'' + path[0] +'\'')
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
        method to update the subtree at a given position
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

def prev_pos(pos):
    i = len(pos) - 1
    cont = True
    while i >= 0 and cont:
        if pos[i] == 'r':
            pos = pos [:i] + 'l' + pos[i+1:]
            cont = False
        else: # pos[i] == 'l'
            pos = pos [:i] + 'r' + pos[i+1:]
        i = i - 1
    if cont: # overflow means one l to much
        return pos[1:]
    else:
        return pos

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
    i = len(pos) - 1
    cont = True
    while i >= 0 and cont:
        if pos[i] == 'l':
            pos = pos [:i] + 'r' + pos[i+1:]
            cont = False
        else: # pos[i] == 'r'
            pos = pos [:i] + 'l' + pos[i+1:]
        i = i - 1
    if cont: # overflow means an additional l
        return pos + 'l'
    else:
        return pos

class Heap():
    def __init__(self):
        self.empty = True
        self.next = ''
    
    @staticmethod
    def __heapify_up(tree,path):
        '''
        helper function to ensure that at any given moment
        the heap's structure is following the rules
        values are moved up the bintree, if necessary
        '''
        if len(path) > 0:
            current = tree._BinTree__subtree_at(path)
            parent_path = path[:len(path)-1]
            parent_tree = tree._BinTree__subtree_at(parent_path)
            if parent_tree.value > current.value:
                current.value,parent_tree.value = parent_tree.value, current.value
                Heap.__heapify_up(tree,parent_path)
    
    @staticmethod
    def __heapify_down(tree,path):
        '''
        helper function to ensure that at any given moment
        the heap's structure is following the rules
        values are moved down the bintree, if necessary
        '''
        current = tree._BinTree__subtree_at(path)
        child_path = next_pos(path)
        child_tree = tree._BinTree__subtree_at(child_path)
        if child_tree.value < current.value:
            current.value,child_tree.value = child_tree.value,current.value
            Heap.__heapify_down(tree,child_path)
    
    def add(self,value):
        '''
        method to add a new entry to the heap
        '''
        if self.empty:
            self.tree = BinTree()
            self.empty = False
        new_node = BinTree.node(BinTree(),value,BinTree())
        self.tree.update_tree_at(self.next,new_node)
        Heap.__heapify_up(self.tree,self.next)

        self.next = next_pos(self.next)
    
    def get_min(self,tree):
        '''
        method that returns the min value in a given heap
        returns None if the heap is empty
        '''
        if tree.empty:
            return None
        else:
            return self.tree.value
    
    def extract_min(self,tree):
        '''
        method to delete the min value in a given heap
        puts the heap's last value into the root node
        and utilizes heapify_down to restore order in the
        galax- heap
        '''
        #get highest value using subtree_at(path)
        #replace old min with update_value_at(path,value)
        temp = self.tree.subtree_at(prev_pos(self.next))
        self.tree.value = temp.value
        #remove the previous entry of the value that was
        #just put into the root spot by calculating a new
        #next position utilizing the prev_pos function
        self.next = prev_pos(self.next)
        self.tree.update_tree_at(self.next,BinTree())
        #utilize heapify_down to out the new min value
        #in its proper spot within the heap
        Heap.__heapify_down(self.tree,'')


h = Heap()

for i in [98,4,76,2,3,45,12,99,104,34]:
    h.add(i)
    print(h.tree)

print(h.get_min(h))
print(h.tree)
h.extract_min(h)
print(h.tree)