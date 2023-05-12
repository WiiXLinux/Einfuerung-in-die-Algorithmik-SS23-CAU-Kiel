import random

from Bintree import BinTree


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
