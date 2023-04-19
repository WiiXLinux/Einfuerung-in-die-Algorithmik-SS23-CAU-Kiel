# PEP 8: E501 was fixed with line-breaking, which makes some statements and comments a bit ugly, we hope you can
# still read them. (like here for example :))

import math
import random
import time


# We reuse this function, because it is already pretty effective. Only creates one list.
# The comments are the same.
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


# Merges a list one time. Makes it much easier to implement mergesort_almost_in_place because the method splits a
# list into chunks of it without creating many lists.
def merge_2(l: list, size: int) -> list:
    # temp is a list containing a sorted partition of l. This means we split l into lists that are of size size.
    temp = []
    # merged_list will be returned.
    merged_list = []
    # Fill temp with the individual lists of size size.
    for b in range(math.ceil(len(l) / size)):
        temp += [l[b * size:(b + 1) * size]]

    # I searched one hour to find out that this was missing... Without it, the mergesort would only work for lists
    # with lengths being in {2^n | n in N} (\in \mathbb N). It basically makes it sure that in the merging after this
    # there does exist a partner for every list in temp to merge with.
    if len(temp) % 2 == 1:
        temp += [[]]
    # Now we go through every of the list pairs in temp and merge them.
    for c in range(len(temp) // 2):
        merged_list += merge(temp[2 * c], temp[2 * c + 1])
    # Finally we return the list that is now one step closer to being sorted.
    return merged_list


# Quick function that swaps the contents of two same sized lists.
# Will raise an exeption if the first list is bigger than the second.
def swap_list(l1: list, l2: list) -> None:
    for i in range(len(l1)):
        a = l1[i]
        l1[i] = l2[i]
        l2[i] = a


# Simple method to generate random integer lists.
# noinspection PyTypeChecker
def random_list(size: int, min: int, max: int) -> list:
    l = [None] * size
    for i in range(len(l)):
        l[i] = random.randint(min, max)
    return l


# A4
# Mergesort that doesn't need so much RAM.
# Named almost in place, because the RAM usage is still linearly congruent to the length of the list.
def mergesort_almost_in_place(l: list) -> list:
    l1 = l + []

    for a in range(math.ceil(math.log2(len(l)))):
        # print(merge_2(l1, 2 ** a))
        l2 = merge_2(l1, 2 ** a)
        swap_list(l1, l2)
    return l1


# It works, it just works.
print(mergesort_almost_in_place([4, 6, 8, 2, 5, 3, 1, 7]))
print(mergesort_almost_in_place([4, 6, 8, 2, 5, 3, 5, 1, 7]))
print(mergesort_almost_in_place(random_list(10, 0, 9)))

def benchmark(func, args):
    before = time.time()
    func(args)
    after = time.time()
    return after - before

# Gives 0.03291511535644531 on my machine.
print(benchmark(mergesort_almost_in_place, random_list(7000, 0, 9)))
