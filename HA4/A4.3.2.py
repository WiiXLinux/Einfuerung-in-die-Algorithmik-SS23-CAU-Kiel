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
        #print(stack)
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
            # n = args[0]
            if n == 0:
                res = args[1]
            else:
                stack.append(('+', 1, []))
                stack.append(('blub', 0, [res, n - 1]))
        elif fun == '*':
            res = 2 * args[0]
        elif fun == '+':
            res = 1 + args[0]

        if res != None:
            if not stack == []:
                pfun, missing_args, args = stack.pop()
                if missing_args == 1:
                    stack.append((pfun, 0, args + [res]))
                else:
                    next_call = stack.pop()
                    stack.append((pfun, missing_args - 1, args + [res]))
                    stack.append(next_call)

    return res


for i in range(10):
    print(bla(i), blablub(i))
