# PEP 8: E501 was fixed with line-breaking, which makes some statements and comments a bit ugly, we hope you can
# still read them. (like here for example :))

import math
import random
import time


# Recursive mergesort as contrast
def mergesort(l: list) -> list:
    if len(l) == 1:
        return l
    else:
        return merge(mergesort(l[:int(len(l) / 2)]), mergesort(l[int(len(l) / 2):]))


# Imperative mergesort from HA3.2
# Sorts a list containing integers by size.
def mergesort2(l: list) -> list:
    # Initialise two helper lists. temp will store the lists before merging, and temp2 will store the lists after
    # merging.
    temp = []
    temp2 = []
    # Fill temp with the elements of the list, but store them as lists with length 1.
    for e in l:
        temp += [[e]]

    # If we want to merge every list in temp at the beginning of this loop, we will need exactly math.ceil(math.log2(
    # len(l))) merges. (We need the ceiling function, because not every list has a length divisible by two)
    for a in range(math.ceil(math.log2(len(l)))):
        # In the case of the list length not being divisible by two, we just add the last element as if it was merged
        # with an empty list.
        if len(temp) % 2 == 1:
            temp2 += [temp[len(temp) - 1]]
        # now go through all pairs of lists in temp and merge them. here the last element will be ignored because we
        # use floor division, which won't be a problem since it was given to temp2 in the last step.
        for i in range(len(temp) // 2):
            temp2 += [merge(temp[2 * i], temp[2 * i + 1])]
        # Prints the list of lists after merging their predecessors. Useful for visualising the example given in the
        # assigment
        print(temp2)
        # Very important to use .copy() so that we don't use the reference to temp2, because our commands are mutative.
        temp = temp2.copy()
        # If it weren't for .copy() one line earlier, we wouldn't just reset temp2, but reset temp as well. We have
        # to reset temp2, so that we can add elements to temp2 while not storing the old elements (which are now in
        # temp).
        temp2 = []
    # returns the first element of temp which is equivalent to the sorted list, since temp now contains a list that
    # is the sorted list. TLDR: Removes some brackets.
    return temp[0]


# Merge function of HA3.1
def merge(l1: list, l2: list) -> list:
    # i and j will be pointing to the first elements of the lists l1 and l2, that have not been inserted into temp.
    j = 0
    i = 0
    # temp will be returned after filling it with a sorted sequence. For now, it will be initialized as a list with
    # same size as the two original lists combined.
    temp = [0] * (len(l1) + len(l2))

    # Stop when we run out of numbers.
    while i + j < len(l1) + len(l2):
        # If we have only run out of numbers from l1...
        if i > len(l1) - 1:
            # ... fill temp with the remaining numbers of l2
            for a in range(i + j, len(temp)):
                temp[a] = l2[a - i]
            return temp
        # If we else have only run out of numbers from l2...
        elif j > len(l2) - 1:
            # ... fill temp with the remaining numbers of l1
            for a in range(i + j, len(temp)):
                temp[a] = l1[a - j]
            return temp
        # If the current number of l2 is bigger than the number of l1...
        if l1[i] < l2[j]:
            # ... insert this number into the new list.
            temp[i + j] = l1[i]
            i += 1
        # If not... (If the number of l1 is bigger or equal than the number of l2)
        else:
            # ... insert that number into the new list.
            temp[i + j] = l2[j]
            j += 1
    # Now we return the completed list.
    return temp


# Simple method to generate random integer lists.
def random_list(size: int, min: int, max: int) -> list:
    l = [None] * size
    for i in range(len(l)):
        l[i] = random.randint(min, max)
    return l


# Prints two examples (with newline for more readability of the output)
print(mergesort2([5, 3, 7, 2, 8, 1, 6, 4, 9]), "\n")
print(mergesort2([5, 3, 7, 2, 8, 1, 6, 4]), "\n")
print(mergesort2(random_list(9, 0, 9)))


def benchmark(func, args):
    before = time.time()
    func(args)
    after = time.time()
    return after - before


# Gives 0.02844524383544922 on my machine. (the print in L41 was removed)
print(benchmark(mergesort, random_list(7000, 0, 9)))

# Gives 0.025584697723388672 on my machine. (the print in L41 was removed)
print(benchmark(mergesort2, random_list(7000, 0, 9)))
