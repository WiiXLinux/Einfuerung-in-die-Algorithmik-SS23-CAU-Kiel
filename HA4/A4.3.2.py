from stack import Stack

def blablub(n):
    stack = Stack()
    stack.push(('bla',0,[n]))
    
    res = None #r
    while stack.top() != None:
        fun, missing_args, args = stack.pop()

        if fun == 'bla':
            print(stack)
            n = args[0]
            if n == 0:
               res = 1
            else:
               stack.push(('*',1,[]))
               stack.push(('blub',1,[1]))
               stack.push(('bla',0,[n-1]))
        elif fun == 'blub':
            print(stack)
            #n = args[0]
            if n == 0:
               res = 1
            else:
               stack.push(('+',1,[]))
               stack.push(('blub',0,[res,n-1]))
        elif fun == '*':
            print(stack)
            res = 2 * res
        elif fun == '+':
            print(stack)
            res = 1 + args[0]
           
        if res != None: 
            if not stack.is_empty():
                parent, missing_args, args = stack.pop()
                if missing_args == 1: 
                    stack.push((parent, 0, res))
                else:
                    next_call = stack.pop()
                    stack.push((parent, missing_args, args + [res]))
                    stack.push((next_call))

    return res

print(blablub(2))
