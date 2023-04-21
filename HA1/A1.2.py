'''
The following code contains a modified version of quicksort using so called three-way-partitioning. 
Best-Case Runtime of this algorithm is O(n log(n)) (n being the number of elements in the list)
Worst-Case Runtime in the unmodified version of this algorithm is O(n^2) in case of lists containing only the same elements. 
In this version however, whenever the currently checked item is equal to the pivot, no swap will happen. 
This is resulting in an optimized runtime of O(n) for any case where all items in a given list are equal to each other.
Furthermore the recursion depth is as low as possible in this version, because in case of an all-same-items-lists 
lt and gt will never move from their start-, respectively, end-positions, so qsort_h() will only call itself once 
for both recursions. 
'''
import random

def swap(l,i,j):
    '''
    this function swaps the elements at indicies i and j in the list l.
    '''
    h = l[i]
    l[i] = l[j]
    l[j] = h

def quicksort(l):
    '''
    Sort given list using three way quicksort
    '''
    def qsort_h(start, end):
        if start < end:
            # Choose pivot randomly
            pivot_idx = random.randint(start, end)
            pivot = l[pivot_idx]
            '''
            Initialize lt and gt as markers for partitions.
            Initialize m as a counting variable.
            '''
            lt = start
            gt = end
            m = start
            while m <= gt:
                                    #compare current item with the pivot
                if l[m] < pivot:    #if current item is smaller than the pivot
                    swap(l, m, lt)  #swap it with the item at the lt-marker
                    m += 1          #move on to ckeck next element
                    lt += 1         #move lt-marker to the right, enlarging the lt-area
                elif l[m] > pivot:  
                    swap(l, m, gt)  #if the current item is larger than the pivot, swap it with the item at the gt marker
                    gt -= 1         #move the gt marker to the left, enlarging the gt-area
                else:
                    m += 1          #if the current item is equal to the pivot, move on to the next element
                                    #all items equal to the pivot will accumulate around the position of the pivot
                                    #effectively generating an equal-area

            #recursively sort the items before and after the pivot.
            qsort_h(start, lt - 1)
            qsort_h(gt + 1, end)

    qsort_h(0, len(l) - 1)

def randlist(n) :
    '''
    generate a list of length n with random elements between 1 and n*100
    '''
    l = []
    for i in range(n):
        l.append(i) #random.randint(1,n*100))
    return l


l = [42] * 42 
print(l)
quicksort(l)
print(l)
