# Contains the same code as in queueClass.py but without the example

class ListElem():
     def __init__(self):
         '''
         construct an empty list elem
         '''
         self.empty = True

     def fill(self,value):
         '''
         fill list elem with value and pointer to a new empty list elem
         '''
         self.empty = False
         self.value = value
         self.next = ListElem()
         return self.next

class Queue():

    def __init__(self):     
        '''
        constructs an empty queue
        '''
        empty_elem = ListElem()
        self.head = empty_elem
        self.end = empty_elem

    def enqueue(self,value):
        '''
        adds value to queue (FIFO-Order)
        '''
        self.end = self.end.fill(value)
    
    def top(self):
        '''
        returns value of oldest element in the queue, without removing
        returns None if queue is empty
        '''
        if self.head.empty:
            return None
        else:
            return self.head.value
       
    def dequeue(self):
        '''
        removes oldest element from the queue and returns its value
        returns None if queue is empty
        '''
        if self.head.empty:
            return None
        else:
            result = self.head.value
            self.head = self.head.next
            return result


