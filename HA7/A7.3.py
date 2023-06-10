'''
In this implementation the order of elements in the heap does
not correspond to the FirstIn-FirstOut principle. This is easy
to see when you look at this example:
(examine all elements with priority of 1, these are highlighted
using the * symbol)

heap.add(1,'prio1.1') *
heap.add(2,'prio2.1')
heap.add(3,'prio3.1')
heap.add(1,'prio1.2') **
heap.add(1,'prio1.3') ***
heap.add(5,'prio5.1')
heap.add(1,'prio1.4') ****
heap.add(3,'prio3.2')
heap.add(1,'prio1.5') *****
heap.add(7,'prio7.1')

this is what is actually stored:
>>>
[
(1, 'prio1.1'), *
(1, 'prio1.2'), **
(1, 'prio1.4'), ****
(1, 'prio1.5'), *****
(1, 'prio1.3'), ***
(5, 'prio5.1'), (3, 'prio3.1'), (3, 'prio3.2'),
(2, 'prio2.1'), (7, 'prio7.1')]

Even though the overall structure of the heap corresponds to
every rule that applies to a heap, the elements with a priority
of 1 are not stored in the same order as they were added to
the heap. This is easily explained by the fact, that the
heapify_up operation of add() switches the elements around
(this is why in this practical example other elements with
different priorities are added to the heap and all values
actually correspond to their priority as well as to the order
in which they were added to the heap).
'''

class Heap():
    '''
    modified implementation where in addition to the value
    a priority is stored for each entry in the heap
    priority-value pairs are stored within a tuple
    tuples are stored within a list
    '''

    def __init__(self):
        self.heap = []

    def __heapify_up(self,i):
        parent_pos = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent_pos]:
            self.heap[i], self.heap[parent_pos] =\
                self.heap[parent_pos], self.heap[i]
            self.__heapify_up(parent_pos)
        
    def __heapify_down(self,i):
        left = i * 2 + 1
        right = left + 1
        cont = True
        while cont and right < len(self.heap):  # test with right, since we know
                                                # that both subtrees exist in loop body
            if self.heap[left]<self.heap[right]:
                min_pos = left
            else:
                min_pos = right
            if self.heap[i] > self.heap[min_pos]:
                #swap(self.heap, i, min_pos)
                self.heap[i], self.heap[min_pos] =\
                    self.heap[min_pos], self.heap[i]
                i = min_pos
                left = i * 2 + 1
                right = left + 1
            else:
                cont = False

        if cont and left < len(self.heap):
            if self.heap[i] > self.heap[left]:
                #swap(self.heap, i, left)
                self.heap[i], self.heap[left] =\
                    self.heap[left], self.heap[i]

    def add(self,prio,v):
        '''
        method to add a priority-value pair to the heap
        '''
        self.heap.append((prio,v))     # constant runtime
        self.__heapify_up(len(self.heap)-1)

    def get_min(self):
        '''
        method that returns the priority and value of the
        root node in the heap
        '''
        return self.heap[0]

    def extract_min(self):
        '''
        method that extracts the entry for the root node
        in the heap and returns its priority and its value
        '''
        if self.heap == []:
            return None
        elif len(self.heap) == 1:
            min = self.heap[0]
            self.heap = []
            return min
        else:
            min = self.heap[0]
            self.heap[0] = self.heap.pop()  # important, since
                                            # constant runtime
            self.__heapify_down(0)
            return min

    def __str__(self):
        '''
        nicer string representation for printing the heap
        '''
        def str_h(i):
            if i < len(self.heap):
                left_res  = str_h(i*2+1)
                right_res = str_h(i*2+2)
                return ('(' + left_res + ',' + 'prio: ' + str(self.heap[i][0]) +
                        ' val: ' + str(self.heap[i][1]) +
                        ',' + right_res + ')')
            else:
                return ''
        
        return str_h(0)
    
    def find_prio(self,prio):
        print(self.heap)
        '''
        method that returns all values
        with a given priority
        '''
        priolist = []
        i = 0
        left = i*2 +1
        right = left +1
        #add first element to priolist, if its prio matches
        if self.heap[0][0] == prio:
            priolist += [self.heap[0][1]]
        #add last element to priolist, if its prio matches
        while right <= len(self.heap):
            #only look at the current nodes child nodes, if
            #their priority is smaller or equal to the prio
            #we're looking for, otherwise increment i, left
            #and right and continue search there
            if prio >= self.heap[i][0]:
                if self.heap[left][0] == prio:
                    priolist += [self.heap[left][1]]
                #make sure, the right node actually exists
                if right <= len(self.heap):
                    if self.heap[right][0] == prio:
                        priolist += [self.heap[right][1]]
                i += 1
                left = i*2 +1
                right = left +1
            else:
                i += 1
                left = i*2 +1
                right = left +1
        return priolist

def rand_list(n):
    res = []
    for i in range(n):
        res.append(i*2) #random.randint(1,n*2))
    return res

heap = Heap()
l = [1,2,3,1,1,5,1,3,1,7,1]
#l = rand_list(10)

'''for x in l:
    heap.add(x,'val')
    print(heap)'''

print(heap.find_prio(10))
print(heap.extract_min())
print(heap.get_min())

'''def heap_sort1(l):
    heap = Heap()
    for x in l:
        heap.add(x)
    res = []
    for i in range(len(l)):
        res.append(heap.extract_min())
    return res'''