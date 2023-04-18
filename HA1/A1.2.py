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
    sort given list with algorithm quicksort.
    '''

    def qsort_h(start,end):
        if start+1 < end:
            m = start + 1
            swap(l,start,random.randint(start,end-1))
            for i in range(m,end):
                if l[i] < l[start]:
                    swap(l,m,i)
                    m = m + 1
            swap(l,start,m-1) # put pivot in the middle
            qsort_h(start,m-1)
            qsort_h(m,end)

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
