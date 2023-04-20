# STILL TODO

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
    sort given list with algorithm quicksort using three-way partitioning.
    '''
    def qsort_h(start,end):
        if start < end:
            '''
            define pivot first using a random index within the list
            then initialize less-than (lt) and greater-than (gt) as markers for partitions
            initialize m as counting variable
            '''
            pivot = l[random.randint(start, end -1)]
            lt = start
            gt = end
            m = start + 1
            while m < gt:
                '''
                in the beginning, m cannot be equal or larger than gt, unless the list contains 0 or 1 element
                if that were the case, the list will be returned as is
                ''' 
                if l[m] < pivot:
                    '''
                    if the current list-item is smaller than the pivot point, it already is on the correct side of the pivot
                    so it can be put in the less-than partition
                    in that case the lt-partition grows by one item, so the lt-marker moves to the right
                    '''
                    swap(l, m, lt)
                    m += 1
                    lt += 1
                elif l[m] > pivot:
                    gt -= 1
                    swap(l, m, gt)
                else:
                    m += 1
                qsort_h(start, lt)
                qsort_h(gt, end)

    qsort_h(0,len(l))

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
