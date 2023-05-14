import copy

# Sorry, aber ich kann listen zum Debuggen besser lesen als die stacks aus der vorlesung, weil dessen str methode scheiße ist.
from stack import Stack


def bla(n):
    if n == 0:
        return 1
    else:
        return 2 * blub(bla(n - 1), 1)


def blub(n, r):
    if n == 0:
        return r
    else:
        return 1 + blub(n - 1, r)


def blablub(n):
    stack = []
    stack.append(('bla', 0, [n]))

    res = None  # r
    while not stack == []:
        print("beginning\t\t", stack)
        fun, missing_args, args = stack.pop()
        assert missing_args == 0

        if fun == 'bla':
            n = args[0]
            if n == 0:
                res = 1
            else:
                stack.append(('*', 1, []))
                stack.append(('blub', 1, [1]))
                stack.append(('bla', 0, [n - 1]))
                res = None
        elif fun == 'blub':
            n = args[0] # Das war richtig
            if n == 0:
                res = args[1]
            else:
                stack.append(('+', 1, []))
                stack.append(('blub', 0, [args[0] - 1, args[1]])) # Hier war die Reihenfolge, glaube ich anders und res statt args[1] machte auch keinen sinn, weil das ja nicht gilt.
                res = None # Das hattest du vergessen
        elif fun == '*':
            res = 2 * args[0]
        elif fun == '+':
            res = 1 + args[0]

        print("second\t\t\t", stack, res)
        c = copy.deepcopy(stack)
        r = copy.copy(res)

        if res != None:
            if not stack == []:
                pfun, missing_args, args = stack.pop()
                if missing_args == 1:
                    stack.append((pfun, 0, args + [res]))
                else:
                    next_call = stack.pop()
                    stack.append((pfun, missing_args - 1, args + [res]))
                    stack.append(next_call)

        if not c == stack or not r == res:
            print("after third\t\t", stack, res)

    return res


print(blablub(3), bla(3))
#for i in range(10): print(bla(i), blablub(i))
