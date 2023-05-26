import random
class Heap():

    def __init__(self):
        self.heap = []

    def __heapify_up(self,i):
        parent_pos = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent_pos]:
            #swap(self.heap, i, parent_pos)
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
        

    def elem(self,value):
        '''
        method to check whether a value exists within a heap
        returns True if the value exists, returns False if it doesn't
        '''
        i = 1
        left = i * 2 + 1
        right = left + 1
        cont = True
        #check the first and the last element first
        if self.heap[0] == value:
            return True
        if self.heap[len(self.heap)-1] == value:
            return True
        #now check all other elements
        while cont and right < len(self.heap):
            if self.heap[i] == value or self.heap[right] == value or self.heap[left] == value:
                return True
            #if the value looked for is smaller than the value
            #of a given node, it is safe to say that the value
            #will not be in one of its subtrees
            if value < self.heap[left]:
                i += 1
                left = i*2 +1
                right = left +1
            elif value < self.heap[right]:
                i += 1
                left = i*2 +1
                right = left +1
            else:
                i+=1
                left = i*2 +1
                right = left +1
        return False
    
    def find_max(self):
        '''
        method to find the max value in a heap
        '''
        #max value can only be located in the last layer
        #so only the last n/2 elements need to be checked
        i = len(self.heap) -1
        max_val = 0
        while i > len(self.heap) / 2:
            if max_val < self.heap[i]:
                max_val = self.heap[i]
            i -= 1
        return max_val
            

    def add(self,v):
        self.heap.append(v)     # constant runtime
        self.__heapify_up(len(self.heap)-1)

    def get_min(self):
        return self.heap[0]

    def extract_min(self):
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
        def str_h(i):
            if i < len(self.heap):
                left_res  = str_h(i*2+1)
                right_res = str_h(i*2+2)
                return ('(' + left_res + ',' + str(self.heap[i]) +
                        ',' + right_res + ')')
            else:
                return ''
        
        return str_h(0)

def rand_list(n):
    res = []
    for i in range(n):
        #res.append(i*2) #
        res.append(random.randint(1,n*2))
    return res

heap = Heap()
#l = [13, 9, 6, 13, 7, 12, 15, 17, 3,56,23,87,92]
l = rand_list(100)

for x in l:
    heap.add(x)
    #print(heap)

'''def heap_sort1(l):
    heap = Heap()
    for x in l:
        heap.add(x)
    res = []
    for i in range(len(l)):
        res.append(heap.extract_min())
    return res'''

print(heap.elem(87))
print(heap.find_max())
print(heap)