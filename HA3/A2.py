'''
realize DEqueue: 
read/write from/to both ends of the queue

enqueue() - add element to BACK
dequeue() - remove element from FRONT
unenqueue() - remove element from BACK
undequeue() - add element to FRONT
front() - read and return FRONT
back() - read and return BACK
'''

class DEQueue():
    class Node:
        def __init__(self, value, prev = None, next = None):
            '''
            initializes a new element in the queue
            expects three parameters, value, prev and next
            prev: references the element at the before-position; 
            by default set to None if there is no parameter given
            next: references the element at the next position
            by default set to None if there is no parameter given
            value: the value stored within this object
            '''
            self.value = value
            self.prev = prev
            self.next = next
    
    def __init__(self):
        '''
        initializes the quere itself
        head: points to front of queue
        end: points to end of queue
        '''
        self.head = None
        self.end = None
    
    def enqueue(self,value):
        '''
        adds an element to the back of the queue
        '''
        #local variable new_node generates a new object
        #next and prev are set to none for now
        new_node = self.Node(value)
        if self.end == None:
            #if the queue is empty, head and end point to 
            #new object added using enqueue()
            self.head = new_node
            self.end = new_node
        else: 
            #if there are already objects stored in queue
            #edit next and prev references of new_node and
            #the previous object
            self.end.next = new_node
            new_node.prev = self.end
            self.end = new_node

    def dequeue(self):
        '''
        remove element from back of the queue
        does nothing if queue is already empty
        '''
        if self.end == None:
            pass
            #could also return None to inform that there are
            #no objects to be removed by using
            # return None
        if self.head == self.end:
            #if there is only on object in the queue
            #this object is removed by setting head and
            #end references to None
            self.head = None
            self.end = None
        else:
            #if there are multiple objects in the queue
            #the current head object is overwritten by the
            #object its next reference points to
            self.head = self.head.next
            #the previous parameter of the current head 
            #object is set to None because now there is 
            #no previous object
            self.head.prev = None

    def unenqueue(self):
        '''
        remove element from the back of the queue
        does nothing if queue is already empty
        '''
        if self.head == None:
            pass
            #could also return None to inform that there is
            #no object to be removed
        if self.head == self.end:
            #in case that there is only one object in the 
            #queue, set head and end pointers to None
            self.head = None
            self.end = None
        else:
            #if there are multiple elements in the queue
            #current end pointer is set to its prev reference
            self.end = self.end.prev
            #next pointer of current end element is set to
            #None because now there is no element after it
            self.end.next = None

    def undequeue(self,value):
        '''
        add an element to the front of the queue
        '''
        #local variable new_node generates a new object
        #next and prev are set to None for now
        new_node = self.Node(value)
        if self.end == None:
            #if the queue is empty, head and end point to 
            #new object added using enqueue()
            self.head = new_node
            self.end = new_node
        else:
            #if there are already elements in the queue
            #the prev reference of the current head object
            #is set to reference new_node
            self.head.prev = new_node
            #new_node's next parameter now points to the 
            #current head object
            new_node.next = self.head
            #finally the head reference points to new_node
            self.head = new_node


    def front(self):
        '''
        returns element at the FRONT of the queue
        return None if queue is empty
        '''
        if self.head == None:
            return None
        else: 
            return self.head.value

    def back(self):
        '''
        returns element at the BACK of the queue
        return None if queue is empty
        '''
        if self.end == None:
            return None
        else:
            return self.end.value

q = DEQueue()
q.enqueue(1)
q.enqueue(2)
q.undequeue(4)

print(q.back())
print(q.front())

q.dequeue()
q.unenqueue()

print(q.back())
print(q.front())