'''
assignment 3.3: Radixsort

LSB variant
basic principle:
- look at LSB of each string
    - have one bucket for each number 0-9
    - put the elements into their corresponding
      bucket
- empty buckets to generate new array
- look at LSB -1 of each string
    - ...
'''

def radixsort(l):
    #turn integers to strings
    l = [str(x) for x in l]
    #get the length of the longest element in the array
    max_length = len(max(l, key=len))

    #if an element in the array has less digit than others,
    #fill them up with zeros from the front
    l = [x.zfill(max_length) for x in l]

    #put elements in their corresponding buckets
    #create a loop to look at each digit of the elements, start 
    #from the highest index (which is the same for each element,
    #because we have filled shorter ones up with zeros)
    for i in range(max_length - 1, -1, -1):

        #initialize a list that serves as buckets. This 
        #list has one element for each digit from 0 to 9.
        #For now these elements are empty, nothing has been 
        #sorted yet
        buckets = [[],[],[],[],[],[],[],[],[],[]]

        #create a loop to inspect the currently looked at
        #digit for each element of the array
        for j in range(len(l)):

            #get the value of the currently looked at digit
            digit = int(l[j][i])

            #put the current element of the array in its 
            #corresponding bucket
            buckets[digit] += [l[j]]

        #put the elements in their new order back into l
        l = [x for bucket in buckets for x in bucket]
        
    #turn the elements back to int; this is optional, but 
    #not pretty because of the zeros elements might have 
    #been filled up with
    l = [int(x) for x in l]
    return l