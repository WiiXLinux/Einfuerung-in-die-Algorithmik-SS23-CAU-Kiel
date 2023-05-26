# Copy of the file used in the lecture with the testing removed

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
        while cont and right < len(self.heap): # test wirh right, since we know 
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
            self.heap[0] = self.heap.pop() # important, since
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
