class LeafTree:
    def __init__(self, val):
        """
        Constructor of LeafTree. Initialises a leaf-tree containing the value val.
        :param val: Value of leaf.
        """
        self.list = [val]

    def __str__(self):
        """
        Converts the leaf-tree to a string.
        :return: String representation of leaf-tree
        """
        # Create empty temporary string.
        temp = ""
        # Convert the value of the leaf-tree, which is probably a list containing other lists, to a dictionary.
        dict = LeafTree.list_to_depth_dict(self.list)
        # Now we go through each key-value pair of the dict and convert each knot or leaf to a string.
        for key in dict:
            isTwo = 1
            # dict[key] is now a list containing all leafs or knots of one layer.
            for item in dict[key]:
                temp += str(item) + " "
                # If the current element is an even one, insert more distance between the next element.
                # This symbolises the inheritance of the branches.
                if isTwo == 2:
                    temp += "\t"
                    isTwo = 1
                else:
                    isTwo += 1
            # The last " \t" is being removed, so that it looks better.
            temp = temp.removesuffix(" \t")
            # After each layer there is a linebreak, so that you can see the layers of the leaf-tree.
            temp += "\n"

        return temp

    def to_list(self):
        """
        "converts" ;) the leaf-tree to a list.
        Simple getter for the value of the leaf-tree, which is the subtrees combined.
        :return: List representation of leaf-tree
        """
        return self.list

    @staticmethod
    def list_to_depth_dict(lst, depth=0, depth_dict=None):
        """
        Converts the list of a leaf-tree into a dictionary representation of the same leaf-tree.
        The method is static, because I didn't want the whole leaf-tree to be passed on each recursion.
        :param lst: A list from a leaf-tree
        :param depth: Leave blank
        :param depth_dict: Leave blank
        :return: Dictionary representation of leaf-tree
        """
        # Checks if the dictionary has not been initialised.
        # If there would have been depth_dict={} in the method parameters,
        # depth_dict wouldn't be empty when reusing the method, making the default argument mutable.
        if depth_dict is None:
            depth_dict = {}
        # If we don't have a list for the current depth, we have to create the key-value pair.
        try:
            depth_dict[depth]
        except:
            depth_dict[depth] = []

        # If the list length is 1 (other case is list length equals to 2), we know that in lst[0] is an actual value
        # or object that doesn't represent another branch. We add this value to our list.
        # (We write "+ lst" and not "+ [lst[0]]")
        if len(lst) == 1:
            depth_dict[depth] = depth_dict[depth] + lst
        # Now it gets recursive, because we know that there are other branches not "visited".
        else:
            # We use "*" as an indicator for a knot.
            depth_dict[depth] += ["*"]
            # As our recursion depth will increase, so does our depth in the leaf-tree.
            depth += 1
            # Now we add both values from the branch to the dict, which also have to be calculated.
            # For that to work we have to pass on our dictionary and our current depth.
            # A nice thing to see is that no information calculated for the dictionary goes missing,
            # because we first "take the left path" and then "take the right path".
            depth_dict = LeafTree.list_to_depth_dict(lst[0], depth, depth_dict)
            depth_dict = LeafTree.list_to_depth_dict(lst[1], depth, depth_dict)
        # After all is complete we return the dict.
        return depth_dict

    @staticmethod
    def branch(left_tree, right_tree):
        """
        Returns a new leaf-tree containing two leaf-trees.
        :param left_tree:
        :param right_tree:
        :return:
        """
        # Initialise the leaf-tree
        temp = LeafTree(None)
        # Set its value to the left and the right subtrees.
        temp.list = [left_tree.list, right_tree.list]
        # Return it.
        return temp

    # TODO: Still in Progress!
    # I am probably giving up on it though because I was sitting on this for 4 hours without break.
    """
    @staticmethod
    def full_leaf_tree(h):
        max_val = int(2 ** (h - 1) - 1)

        temp = [0]
        to_return = LeafTree(None)

        couter = 0
        print(range(max_val))

        to_return = LeafTree.branch()

        to_return.list = temp
        return to_return
        """


# Tests
lt1 = LeafTree(1)
lt2 = LeafTree.branch(LeafTree(1), LeafTree(2))
lt3 = LeafTree.branch(LeafTree(1), LeafTree.branch(LeafTree.branch(LeafTree(2), LeafTree.branch(LeafTree.branch(
      LeafTree(3), LeafTree(4)), LeafTree.branch(LeafTree(5), LeafTree(6)))), LeafTree(7)))

print("Testing str(LeafTree): ")
print("Printing first leaf-tree")
print(lt1)
print("Printing second leaf-tree")
print(lt2)
print("Printing last leaf-tree")
print(lt3)
print()

print("Testing LeafTree.to_list()")
print("Printing first leaf-tree")
print(lt1.to_list())
print("Printing second leaf-tree")
print(lt2.to_list())
print("Printing last leaf-tree")
print(lt3.to_list())
