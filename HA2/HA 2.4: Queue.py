'''
assignment 2.4: Queue

implementation of new methods using     classes:        dicts:
    list_to_queue() ;;;                 70 - 75         164 - 170
    queue_to_list() ;;;                 77 - 87         172 - 180                      
    undequeue() ;;;                     89 - 97         182 - 190
    unequeue() ;;;                      99 - 119        192 - 209

More efficient runtime on unequeue() can be achieved if the way the queue is 
constructed allowed for keeping track of how many items are waiting. The way 
unenqueue() is currently implemented is not efficient: the program needs to 
iterate over every element of the queue twice in order to remove the element 
in the end.
One of those those passes could be avoided if there was an element-counter
attribute within the class that is increased or decreased depending on the 
operation and runtime can be reduced to O(n), n being the number of elements
currently waiting in queue.
It may also be possible to implement a queue using nested lists. That way
it would be quite easy to remove the element at the end of the list by 
utilizing negative indexing (-1 accesses the last item in the list).
'''

########
#USING CLASSES
########

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

######
#USING DICTS
######

def empty_queue():
    '''
    constructs an empty queue
    '''
    empty_elem = {}
    return {'head' : empty_elem, 'end' : empty_elem}

def enqueue(value,queue):
    '''
    adds value to queue (FIFO-Order)
    '''
    old_end = queue['end']
    old_end['value'] = value
    empty_elem = {}
    old_end['next'] = empty_elem
    queue['end'] = empty_elem
    
def top(queue):
    '''
    returns value of oldest element in the queue, without removing
    returns None if queue is empty
    '''
    if queue['head'] == {}:
        return None
    else:
        return queue['head']['value']
       
def dequeue(queue):
    '''
    removes oldest element from the queue and returns its value
    returns None if queue is empty
    '''
    if queue['head'] == {}:
        return None
    else:
        result = queue['head']['value']
        queue['head'] = queue['head']['next']
        return result

def list_to_queue(queue, list):
    '''
    turns a given list into a queue
    '''
    for elem in list:
        enqueue(elem, queue)
    return queue

def queue_to_list(queue, list):
    '''
    turns a queue into list
    '''
    while top(queue) != None:
        list += [top(queue)]
        dequeue(queue)
    if top(queue) == None:
        return (queue, list)

def undequeue(value, queue):
    '''
    adds an element to the front of the queue
    '''
    old_head = queue['head']
    empty_elem = {}
    empty_elem['value'] = value
    empty_elem['next'] = old_head
    queue['head'] = empty_elem

def unenqueue(queue):
    #count how many elements there are in the queue, iterating using current as mutable 
    #object and currentcount as counter of how many steps the program needs to make to 
    #remove the last element
    current = queue['head']
    currentcount = 0
    while current['next'] != queue['end']:
        #count for as many times as there are elements that are not the end of the queue
        current = current['next']
        currentcount += 1
    #reset current to its default state at the beginning of the queue, so we can count 
    #into the queue again, in order to stop on element before the end. this is the 
    #element we want to remove
    current = queue['head']
    while currentcount > 1:
        current = current['next']
        currentcount -= 1
    current['next'] = {}
