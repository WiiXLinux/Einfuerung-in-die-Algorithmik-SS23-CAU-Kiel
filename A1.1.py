# PEP 8: E501 was fixed with line-breaking, which makes some statements and comments a bit ugly, we hope you can
# still read them. (like here for example :))

import random


# Simple method to generate random lists
def random_list(size: int, min: int, max: int) -> list:
    l = [None] * size
    for i in range(len(l)):
        l[i] = random.randint(min, max)
    return l


# Simple ring-swap for list elements
def swap_lst(l: list, a: int, b: int) -> None:
    temp = l[a]
    l[a] = l[b]
    l[b] = temp


# Sorts a list containing integers by size with a Hungarian variation of Quicksort.
def hungarian_quicksort(l: list) -> list:
    # lists with a length smaller than 2, so lists with a length 1 or 0, are sorted by definition.
    if len(l) < 2:
        return l

    # so that our function is definitely non-mutative. Important, because we will swap some elements in it.
    l = l + []

    # The sorted list should have the same size as the unsorted list.
    final_list = [None] * len(l)

    # initialise the bounds for the comparisons.
    pivot_index = 0
    scanner_index = len(l) - 1

    # mode: Scan from right or Scan from left
    mode = True

    # Uncomment if necessary for making sense of the algorithm.
    # print(l, pivot_index, scanner_index)

    # We can only exit from this endless loop, if we return the sorted list, which we will.
    while True:
        while mode:
            # When pivot_index = scanner_index, so when there is no partner for the pivot to swap, we split the list
            # in two and sort them recursively.
            if pivot_index == scanner_index:
                # The position of the pivot in the sorted list is known, but we still have to sort the left and right
                # half of the list. When the recursive subprograms terminate, we will return the sorted list,
                # and break out of the endless loop.
                return hungarian_quicksort(l[:pivot_index]) + [l[pivot_index]] + hungarian_quicksort(
                    l[(pivot_index + 1):])

            # If we found a partner for the pivot, swap them. ! Also don't forget to swap the indexes of them.
            if l[pivot_index] > l[scanner_index]:
                # Swap partner and pivot
                swap_lst(l, pivot_index, scanner_index)

                # Swap their indexes, so they make sense via another ring-swap.
                a = pivot_index
                pivot_index = scanner_index
                scanner_index = a

                # After swapping, we will scan from left to right, searching for partners bigger than our pivot
                mode = False
                break
            # If we just didn't swap, we search for another possible partner for the pivot. This partner could be the
            # left neighbor of the former, so we iterate scanner_index + 1. We will maximally iterate to pivot_index,
            # and then we know there is no partner for the pivot for he is placed at the right index.
            scanner_index -= 1
        # Uncomment if necessary for making sense of the algorithm.
        # print(l, pivot_index, scanner_index)
        while not mode:
            # When pivot_index = scanner_index, so when there is no partner for the pivot to swap, we split the list
            # in two and sort them recursively.
            if pivot_index == scanner_index:
                # The position of the pivot in the sorted list is known, but we still have to sort the left and right
                # half of the list. When the recursive subprograms terminate, we will return the sorted list,
                # and break out of the endless loop.
                return hungarian_quicksort(l[:pivot_index]) + [l[pivot_index]] + hungarian_quicksort(
                    l[(pivot_index + 1):])

            # If we found a partner for the pivot, swap them. ! Also don't forget to swap the indexes of them.
            if l[pivot_index] < l[scanner_index]:
                # Swap partner and pivot
                swap_lst(l, pivot_index, scanner_index)

                # Swap their indexes, so they make sense via another ring-swap.
                a = pivot_index
                pivot_index = scanner_index
                scanner_index = a

                # After swapping, we will scan from right to left again, searching for partners smaller than our pivot.
                mode = True
                break
            # If we just didn't swap, we search for another possible partner for the pivot. This partner could be the
            # right neighbor of the former, so we iterate scanner_index + 1. We will maximally iterate to pivot_index,
            # and then we know there is no partner for the pivot for he is placed at the right index.
            scanner_index += 1
        # Uncomment if necessary for making sense of the algorithm.
        # print(l, pivot_index, scanner_index)

        # After all of this we will repeat until the pivot is placed in the right position.


# Prints the sorted list of a randomly generated list with the hungarian quicksort.
print(hungarian_quicksort(random_list(10, 0, 9)))
# Example used in the video.
print(hungarian_quicksort([3, 0, 1, 8, 7, 2, 5, 4, 9, 6]))
