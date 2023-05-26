import random
import timeit


class SearchTree:
    """
    Class implementing search trees, without balancing
    """

    def __init__(self, left=None, value=None, right=None):
        """
        constructs either an empty Searchtree or a node in a Searchtree with subtrees
        left and right,
        call: SearchTree() for empty BinTree
              SearchTree(tl,v,tr) for node
        """
        if left is None:
            self.empty = True
            self.height = 0  # Height should be 0
        else:
            self.empty = False
            self.height = 1  # Height should be 1
            self.left = left
            self.value = value
            self.right = right

    def _update_height(self):
        """
        auxiliary function for updating the height of a node.
        """
        self.height = max(self.left.height, self.right.height) + 1

    def insert(self, v):
        """
        inserts the given value v into the searchtree
        returns False, if value already occurs, otherwise True
        """
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

    def elem(self, v):
        """
        checks whether v occurs in th search tree
        """
        if self.empty:
            return False
        elif v == self.value:
            return True
        elif v < self.value:
            return self.left.elem(v)
        else:
            return self.right.elem(v)

    def elem_iter(self, v):
        """
        iterative version of elem
        """
        st = self
        while not st.empty and v != st.value:
            if v < self.value:
                st = st.left
            else:
                st = st.right
        return not st.empty

    def __str__(self):
        """
        nice string representation of a search tree, mainly useful for
        debugging
        """
        if self.empty:
            return '_'
        elif self.left.empty and self.right.empty:
            return str(self.value)
        else:
            return ('(' + str(self.left) + ',' + str(self.value) +
                    ',' + str(self.right) + ')')


class PriorityQueue:
    def __init__(self):
        self.tree = None
        self.empty = True
        self.next = ''

    @staticmethod
    def __heapify_up(tree, path):
        """
        helper function to ensure that at any given moment
        the heap's structure is following the rules
        values are moved up the SearchTree, if necessary
        """
        if len(path) > 0:
            current = PriorityQueue.__subtree_at(tree, path)
            parent_path = path[:len(path) - 1]
            parent_tree = PriorityQueue.__subtree_at(tree, parent_path)
            if parent_tree.value > current.value:
                current.value, parent_tree.value = parent_tree.value, current.value
                PriorityQueue.__heapify_up(tree, parent_path)

    @staticmethod
    def __heapify_down(tree, path):
        """
        helper function to ensure that at any given moment
        the heap's structure is following the rules
        values are moved down the SearchTree, if necessary
        """
        current = PriorityQueue.__subtree_at(tree, path)
        child_path = PriorityQueue.next_pos(path)
        child_tree = PriorityQueue.__subtree_at(tree, child_path)

        # If the child_tree doesn't exist, like for example when we remove the last element of a PriorityQueue, there is
        # no reason to heapify.
        if child_tree is None:
            return False

        if child_tree.value < current.value:
            current.value, child_tree.value = child_tree.value, current.value
            PriorityQueue.__heapify_down(tree, child_path)

    @staticmethod
    def prev_pos(pos):
        """
        Helper function previously used.
        """
        i = len(pos) - 1
        cont = True
        while i >= 0 and cont:
            if pos[i] == 'r':
                pos = pos[:i] + 'l' + pos[i + 1:]
                cont = False
            else:  # pos[i] == 'l'
                pos = pos[:i] + 'r' + pos[i + 1:]
            i = i - 1
        if cont:  # overflow means one l to much
            return pos[1:]
        else:
            return pos

    @staticmethod
    def next_pos(pos):
        """
        Helper function previously used.
        compute next position in Search trees or search trees
        the order is as follows:
        '', 'l', 'r', 'll', 'lr', 'rl', 'rr', 'lll', 'llr', ...
        """
        i = len(pos) - 1
        cont = True
        while i >= 0 and cont:
            if pos[i] == 'l':
                pos = pos[:i] + 'r' + pos[i + 1:]
                cont = False
            else:  # pos[i] == 'r'
                pos = pos[:i] + 'l' + pos[i + 1:]
            i = i - 1
        if cont:  # overflow means an additional l
            return pos + 'l'
        else:
            return pos

    @staticmethod
    def node(left, value, right):
        """
        statical method to construct a node in the Searchtree
        """
        tree = SearchTree()
        tree.empty = False
        tree.left = left
        tree.value = value
        tree.right = right
        return tree

    @staticmethod
    def __subtree_at(of_tree, path):
        """
        method for accessing subtree at given position
        not supposed to be used from outside, since subtree is not copied
        internally needed to mutate the subtree
        """
        tree = of_tree
        while path != '' and not tree.empty:
            if path[0] == 'l':
                tree = tree.left
            elif path[0] == 'r':
                tree = tree.right
            else:
                raise Exception('no valid path: containing \'' + path[0] + '\'')
            path = path[1:]

        if path == '':
            return tree
        else:
            return None

    @staticmethod
    def subtree_at(of_tree, path):
        """
        method to select a subtree from outside the class
        a copy of the selected subtree is returned
        """
        subtree = PriorityQueue.__subtree_at(of_tree, path)
        if subtree is None:
            return None
        else:
            return PriorityQueue.copy(subtree)

    @staticmethod
    def update_value_at(tree, path, value):
        """
        method to update the value at a given position
        returns old value in case of success and None otherwise
        """
        subtree = PriorityQueue.__subtree_at(tree, path)
        if subtree is not None:
            old_value = subtree.value
            subtree.value = value
            return old_value
        else:
            return None

    @staticmethod
    def update_tree_at(of_tree, path, tree):
        """
        method to update the subtree at a given position
        returns a boolean indicating whether the update was successful
        """
        subtree = PriorityQueue.__subtree_at(of_tree, path)
        if subtree is not None:
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

    @staticmethod
    def copy(of_tree):
        """
        make a deep copy of the given tree object.
        only subtrees are copied, values are shared
        """
        if of_tree.empty:
            return SearchTree()
        else:
            return SearchTree(PriorityQueue.copy(of_tree.left), of_tree.value, PriorityQueue.copy(of_tree.right))

    # All static methods to here are helper functions.

    def add(self, value):
        """
        method to add a new entry to the heap
        """
        if self.empty:
            self.tree = SearchTree()
            self.empty = False
        new_node = PriorityQueue.node(SearchTree(), value, SearchTree())
        PriorityQueue.update_tree_at(self.tree, self.next, new_node)
        PriorityQueue.__heapify_up(self.tree, self.next)

        self.next = PriorityQueue.next_pos(self.next)

    def get_min(self, tree):
        """
        method that returns the min value in a given heap
        returns None if the heap is empty
        """
        if tree.empty:
            return None
        else:
            return self.tree.value

    def extract_min(self):
        """
        method to delete the min value in a given heap
        puts the heap's last value into the root node
        and utilizes heapify_down to restore order in the
        galax- heap
        """
        if self.empty:
            return None
        # get the highest value using subtree_at(path)
        # replace old min with update_value_at(path,value)
        temp = PriorityQueue.subtree_at(self.tree, PriorityQueue.prev_pos(self.next))
        self.tree.value = temp.value
        # remove the previous entry of the value that was
        # just put into the root spot by calculating a new
        # next position utilizing the prev_pos function
        self.next = PriorityQueue.prev_pos(self.next)
        PriorityQueue.update_tree_at(self.tree, self.next, SearchTree())
        # utilize heapify_down to out the new min value
        # in its proper spot within the heap
        PriorityQueue.__heapify_down(self.tree, '')


# Testing
def rand_list(n):
    res = []
    for i in range(n):
        # Notice, that there is the possibility that the same value is used multiple times.
        res.append(random.randint(1, n * 2))
    return res


"""
h = PriorityQueue()

l = rand_list(12)
for i in l:
    h.add(i)

print(h.get_min(h))
print(h.tree)
# If there is a duplicate of the value, the value still will be removed only once, so don't worry when after extract_min
# there is still the value of the same minimum inside the PriorityQueue.
h.extract_min()
print(h.tree)
"""


# Second task:
from heap import Heap

heap1 = Heap()
heap2 = PriorityQueue()

l1 = rand_list(200)
print(l1)

timeDiff = timeit.default_timer()
for i in l1:
    heap1.add(i)

print("Time elapsed after adding into list Heap: " + str(timeit.default_timer() - timeDiff))

timeDiff = timeit.default_timer()  # Reset timer.
for i in l1:
    heap1.extract_min()

print("Time elapsed after removing from list Heap: " + str(timeit.default_timer() - timeDiff))


print(heap1.heap)  # -> []

timeDiff = timeit.default_timer()  # Reset timer.
for i in l1:
    heap2.add(i)

print("Time elapsed after adding into SearchTree Heap: " + str(timeit.default_timer() - timeDiff))

timeDiff = timeit.default_timer()  # Reset timer.
for i in l1:
    heap2.extract_min()

print("Time elapsed after removing from SearchTree Heap: " + str(timeit.default_timer() - timeDiff))

print(heap2.tree)  # -> _

"""
Hieraus erschließt sich, dass unsere implementierung um einiges langsamer ist, als die Listen-Implementierung.
Dies ergibt jedoch auch viel Sinn, schließlich werden bei der Listenimplementierung viel weniger Objekte erzeugt, die
dann auch noch viel weniger Speicher reservieren und aufrufen müssen.
Unsere Implementierung erstellt viel zu viele Objekte und verwendet laufzeittechnisch längere und mehr Methoden.
Ich bin erstaunt, dass unsere implementierung beim hinzufügen noch so schnell war um ehrlich zu sein
("nur" 10 mal langsamer, wow).
"""
