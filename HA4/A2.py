import random

from Bintree import BinTree
from stack import Stack


def max(tree: BinTree) -> int:
    """
    Recursive approach utilising a setting sub method to find the maximal value of a binarytree
    :param tree: Binary tree to scan
    :return: Maximal value of tree
    """

    # Subroutine, will set return_value[0] to the value that is the smallest value yet.
    def __max(tree: BinTree) -> None:
        # Get the reference of return_value that is declared below this method and give it a name.
        return_value[0] = return_value[0]
        # If the current tree is empty, our return_value we break.
        # Notice, that we don't have to set return_value to anything because it's already the current max.
        # Also prevents Exceptions, because if tree.empty then there are no tree.left and tree.right.
        # I added the "tree is None" because something didn't work in my random_bintree method and I don't know why, but
        # it creates random bin_trees have a NoneType object on their right, you can see that later when
        # I create some examples and test them, because I will print them. Anyway I left the method for testing.
        if tree is None or tree.empty:
            return
        # If there is a bigger fish, eat the smaller one.
        if tree.value == None:
            pass
        elif tree.value > return_value[0]:
            return_value[0] = tree.value
        # Run the recursion again for the left subtree and for the right subtree.
        __max(tree.left)
        __max(tree.right)

    # Set a temporary return_value to 0.
    return_value = [0]
    # Calculate the maximum
    __max(tree)
    # Return it.
    return return_value[0]


def random_bintree(size: int) -> BinTree:
    """
    Here something went wrong.
    Should create a fully random bintree which has the height: size
    :param size: Height of the bintree
    :return: Random bintree with height size
    """

    def recursion(tree: BinTree, current_length: int, _size: int) -> BinTree:
        """
        Sub method used in recursion
        :param tree: Current bintree
        :param current_length: Current height of the bintree
        :param _size: Size that it should be
        :return: Temporary bintree
        """
        # If the tree is already big enough, return it.
        if _size <= current_length:
            return tree
        # If not, let it grow.
        current_length += 1
        # Flip a coin:
        # Is it heads...
        if bool(random.randint(0, 1)):
            # ... make two new branches with random sub-bintrees and values.
            return BinTree(recursion(tree, current_length, _size), random.randint(0, 20),
                           BinTree(recursion(tree, current_length, _size)))
        # Is it tails, don't make a new branch, but give the current subtree a value.
        tree.value = random.randint(0, 1)
        return recursion(tree, current_length, _size)

    # Return the soon-to-be calculated random tree.
    return recursion(BinTree(), 0, size)


test = random_bintree(5)
print(test)
print(max(test))


# For the next task we'll use the method given in the assigment:
def max2(nested_l):
    '''
    computes the maximum number within a arbitrary nested list of numbers
    '''

    def max_h(nested_l):
        print(nested_l)
        if type(nested_l) is list and len(nested_l) > 0:
            max_h(nested_l[0])
            max_h(nested_l[1:])
        elif type(nested_l) is int:
            if nested_l > max[0]:
                max[0] = nested_l

    max = [0]
    max_h(nested_l)
    return max[0]

# TODO: Comment, add more tests
def max2_iter(nested_l):
    stack = Stack()
    stack.push(("max2", 0, [nested_l]))
    result = 0

    while not stack.is_empty():
        fun, missing_args, args = stack.pop()
        assert missing_args == 0
        if fun == "max2":
            nested_l = args
            if type(nested_l) is list and len(nested_l) > 0:
                stack.push(("max2", 0, nested_l[0]))
                stack.push(("max2", 0, nested_l[1:]))
                result = 0
            # Here we've shortened the original expression a bit.
            elif type(nested_l) is int and nested_l > result:
                result = nested_l
        else:
            raise Exception("Something went tits up with the golden order")
        if result is None:
            if not stack.is_empty():
                pfun, pmissing_args, pargs = stack.pop()
                if pmissing_args == 1:
                    stack.push((pfun, 0, pargs + [result]))
                else:
                    nextsubcomp = stack.pop()
                    stack.push((pfun, pmissing_args - 1, pargs + [result]))
                    stack.push(nextsubcomp)

    return result


test2 = [[2, 3, [6]], 4, [2, 5], []]
print(max2(test2))
print(max2_iter(test2))
