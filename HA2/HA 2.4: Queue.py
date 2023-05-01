'''
assignment 2.4: Queue

implementation of new methods using classes:
    list_to_queue() ;;; lines 50 - 55
    queue_to_list() ;;; lines 58 - 68
    undequeue() ;;; lines 71 - 78
    unequeue() ;;; lines 82 - 102

'''

class Queue():

    def __init__(self):     
        '''
        constructs an empty queue
        '''
        empty_elem = {}
        self.head = empty_elem
        self.end = empty_elem

    def enqueue(self,value):
        '''
        adds value to queue (FIFO-Order)
        '''
        old_end = self.end
        old_end['value'] = value
        empty_elem = {}
        old_end['next'] = empty_elem
        self.end = empty_elem
    
    def top(self):
        '''
        returns value of oldest element in the queue, without removing
        returns None if queue is empty
        '''
        if self.head == {}:
            return None
        else:
            return self.head['value']
       
    def dequeue(self):
        '''
        removes oldest element from the queue and returns its value
        returns None if queue is empty
        '''
        if self.head == {}:
            return None
        else:
            result = self.head['value']
            self.head = self.head['next']
            return result
    
    def list_to_queue(self, list):
        '''
        takes a list and turns it into a queue
        '''
        for i in list:
            self.enqueue(i)
    
    def queue_to_list(self, l):
        '''
        takes a queue and turns it into a list
        '''
        while self.top() != None:
            #as long as there a elements waiting in the queue, add them to the list
            l += [self.top()]
            self.dequeue()
        #as soon as there are no elements waiting in the queue, return both list and queue
        if self.top() == None:
            return (l, self)
        
    def undequeue(self, value):
        '''
        adds an element to the front of the queue
        '''
        old_head = self.head
        empty_elem = {}
        empty_elem['value'] = value
        empty_elem['next'] = old_head
        self.head = empty_elem

    def unenqueue(self):
        '''
        removes value from queue at the end
        '''
        #count how many elements there are in the queue, iterating using current as mutable 
        #object and currentcount as counter of how many steps the program needs to make to 
        #remove the last element
        current = self.head
        currentcount = 0
        while current['next'] != self.end:
            #count for as many times as there are elements that are not the end of the queue
            current = current['next']
            currentcount += 1
        #reset current to its default state at the beginning of the queue, so we can count 
        #into the queue again, in order to stop on element before the end. this is the 
        #element we want to remove
        current = self.head
        while currentcount > 1:
            current = current['next']
            currentcount -= 1
        current['next'] = {}
