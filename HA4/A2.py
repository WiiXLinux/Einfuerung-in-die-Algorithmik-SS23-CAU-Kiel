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


# print(test)
# print(max(test))


# For the next task we'll use the method given in the assigment:
def max2(nested_l):
    '''
    computes the maximum number within a arbitrary nested list of numbers
    '''

    def max_h(nested_l):
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
def max2_iter(nested_l: list) -> int:
    """
    Iterative implementation of max2.
    :param nested_l: Binary tree as list to be searched.
    :return: Maximal value.
    """
    # We don't need no...
    # list mutation...
    nested_l = nested_l + []
    # Create an empty stack to push and pop:
    # operation keys, the number of missing arguments and inputs for the operations.
    stack = []
    # Push the operation to be completed with the required arguments.
    # In the beginning no arguments are missing because we don't know yet that we will probably need more.
    # As time unfolds, so will the operations.
    stack.append(("max2", 0, [nested_l]))
    # Result will carry the result of all operations.
    # Will return to None when there is a method called that doesn't change the result,
    # like for example the list splitting in recursive mergesort.
    result = None
    # Initiate a temporary result with 0.
    # Because in the original max2 there was assumed that the minimal value is 0, we will here too.
    tmpmax = 0
    # Repeat following steps until there are no calculations to be made.
    while len(stack) > 0:
        # Receive ToS.
        fun, missing_args, args = stack.pop()
        # This should be the case since the only method we "call" in our implementation is max2.
        # The Exception in line 152 is with that fact basically a detector for cosmic radiation.
        if fun == "max2":
            # Get basically the nested_l that would be given by a recursive call. Just using args is also ok, but
            # this makes it a bit more readable, what we're doing.
            nested_l = args
            # This is the same as before, we look if nested_l is still a list containing more than 0 objects,
            # We have to "call" max2 again in the future.
            if type(nested_l) is list and len(nested_l) > 0:
                # We're doing this by pushing the arguments needed, as well as their operations and missing arguments
                # (which are both 0 after calculation), to the stack. We also have to swap the order of operations.
                stack.append(("max2", 0, nested_l[1:]))
                stack.append(("max2", 0, nested_l[0]))
                # Reset result to the value of this calculation which is None.
                result = None
            # Here we've shortened the original expression a bit. Still does the same...
            elif type(nested_l) is int and nested_l > tmpmax:
                # Basically returning nested_l.
                result = nested_l
                # Update tmpmax
                tmpmax = result
        # This here is the cosmic radiation detector we mean.
        else:
            raise Exception("Unknown operation: " + fun + "\nsomething went really really wrong if you see this...")
        # If the last calculation didn't "return" anything, we have to swap two operations.
        if result is not None:
            # If there are still calculations to be made:
            if len(stack) > 0:
                # We prepare the parent function, missing arguments number and arguments
                # to swap them with the current ToS.
                pfun, pmissing_args, pargs = stack.pop()
                if pmissing_args == 1:
                    # We know there should not be any arguments more left at this point for the function
                    # that we want to execute, so we don't write "pmissing_args - 1"
                    stack.append((pfun, 0, pargs + [result]))
                else:
                    # If not, we just swap the parents with their parents that turn into their children...
                    nextsubcomp = stack.pop()
                    stack.append((pfun, pmissing_args - 1, pargs + [result]))
                    stack.append(nextsubcomp)
    # Now we finally have our result.
    result = tmpmax
    return result


# Here are some tests:
test2 = [[2, 3, [6]], 4, [2, 5], []]
test3 = [[2, 3, [4]], 4, [2, 5], [], [[[[5, 3, [9]], 4, [2, 5], [], 3, [6]], 4, [2, 5], []], [2, 24, [20]], 4, [2, 5]]]
test4 = [[2], [[5], [[1], [9]]], [2, 5], [], [[[[5, 3, [9]], 4, [2, 5], [], 3, [6]]]]]

assert max2(test2) == max2_iter(test2)  # -> 6
assert max2(test3) == max2_iter(test3)  # -> 24
assert max2(test4) == max2_iter(test4)  # -> 9
