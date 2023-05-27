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
        

    def delete_at(self, pos):
        '''
        method to delete a value at a given position
        '''
        #positions are given via the index
        #make sure the position exists
        if pos == len(self.heap) - 1:
            self.heap.pop()
        elif pos < len(self.heap):
            #pop element on position
            temp = self.heap[pos]
            self.heap[pos] = self.heap[len(self.heap)-1]
            #heapify_down largest element
            self.heap.pop(len(self.heap)-1)
            self.__heapify_down(pos)
            return temp
        elif len(self.heap) == 1 and pos == 1:
            temp = self.heap[0]
            self.heap = []
            return temp
        #if the position does not exist, return False to hint
        #that the operation was not successful
        else:
            return False
            #if the function should instead return nothing
            #in case the operation was unsuccessful because
            #the position does not exist: pass

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
            if value < self.heap[i]:
                if self.heap[right] == value or self.heap[left] == value:
                    return True
                i += 2
                left = i*2 +1
                right = left +1
            else:
                i += 1
                left = i*2 +1
                right = left +1
        return False

    def delete(self, value):
        '''
        method to delete a given value
        returns true if the value existed in the Heap
        returns false if the value did not exists in
        the heap and therefore could not be deleted
        '''
        i = 1
        left = i * 2 + 1
        right = left + 1
        #if the value is the first or last element in the heap
        #easy to delete
        if self.heap[0] == value:
            self.extract_min()
            return True
        if self.heap[len(self.heap)-1] == value:
            self.heap.pop(len(self.heap)-1)
            return True
        #now check all other elements
        while right < len(self.heap):
            if self.heap[i] == value:
                #pop element on position
                self.heap[i] = self.heap[len(self.heap)-1]
                #heapify_down largest element
                self.heap.pop(len(self.heap)-1)
                self.__heapify_down(i)
                return True
            elif self.heap[right] == value:
                #pop element on position
                self.heap[right] = self.heap[len(self.heap)-1]
                #heapify_down largest element
                self.heap.pop(len(self.heap)-1)
                self.__heapify_down(right)
                return True
            elif self.heap[left] == value:
                #pop element on position
                self.heap[left] = self.heap[len(self.heap)-1]
                #heapify_down largest element
                self.heap.pop(len(self.heap)-1)
                self.__heapify_down(left)
                return True
            #if the value looked for is smaller than the value
            #of a given node, it is safe to say that the value
            #will not be in one of its subtrees
            if value < self.heap[i]:
                if self.heap[right] == value:
                    self.heap[right] = self.heap[len(self.heap)-1]
                    self.heap.pop(len(self.heap)-1)
                    self.__heapify_down(right)
                    return True
                elif self.heap[left] == value:
                    self.heap[left] = self.heap[len(self.heap)-1]
                    self.heap.pop(len(self.heap)-1)
                    self.__heapify_down(left)
                    return True
                i += 2
                left = i*2 +1
                right = left +1
            else:
                i+=1
                left = i*2 +1
                right = left +1
        return False

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
        res.append(random.randint(1,n*2)) #random.randint(1,n*2))
    return res

heap = Heap()
l = [13, 9, 6, 13, 7, 12, 15, 17]
#l = rand_list(15)

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

#print(heap.elem(20))
#print(heap.elem2(24))
print(heap)
#print(heap.delete(6))
heap.delete_at(7)
print(heap)