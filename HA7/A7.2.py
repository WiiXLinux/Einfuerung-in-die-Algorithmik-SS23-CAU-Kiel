import timeit


# Copied from to_01list.py
def to_01list(n):
    """
    convert n into binary representation
    list of bits starts with lsb.
    """
    if n == 0:
        '''
        strange case, because zero is not the empty word, but 0
        '''
        return [0]
    else:
        res = []
        while n > 0:
            res.append(n % 2)
            n = n // 2
        return res


# Task 1:
def bin_inc(list_to_increment: list):
    """
    Non-mutative bitwise incrementation of a binary number represented as a list.
    Runtime analysis:
    n is proportional to the length of list_to_increment:
    Has O(n) runtime in the average case and maximal case.
    Has O(1) runtime in the minimal case that the list_to_increment is empty or has only one element.
    :param list_to_increment: the list to increment :return: list_to_increment + 1
    """
    # Constant runtime
    new_list = [0] * len(list_to_increment)
    # Constant runtime
    carry = 1

    # Repeat len(list_to_increment) times. In case of carry == 0 after addition,
    # there will be constantly fewer operations (since we don't have to add anymore),
    # which doesn't matter for the runtime analysis.
    for i in range(len(list_to_increment)):
        # Constant runtime
        new_list[i] = (list_to_increment[i] ^ carry)  # 0 ^ 0 -> 0, 1 ^ 0 -> 1, 1 ^ 1 -> 0, 0 ^ 0 -> 0
        # Constant runtime
        carry = list_to_increment[i] & carry
        # If there is no carry left over (there was an addition with exact result 0 or 1) then fill the rest and return.
        # Comparison has constant runtime
        if carry == 0:
            # Has O(n) whereas n = len(list_to_increment) - i.
            new_list[i + 1:] = list_to_increment[i + 1:]
            # Constant runtime
            return new_list
    # Constant runtime
    if carry == 1:
        # Constant runtime
        new_list.append(1)
    # Constant runtime
    return new_list


# Tests:
# print(bin_inc([0, 1, 1]))  # -> [1, 1, 1]
# print(bin_inc([1, 0, 1]))  # -> [0, 1, 1]

# Print binary numbers from 0 + 1 to 15 + 1
# for i in range(0, 16):
# print(bin_inc(to_01list(i)))


# Task 2:
def bin_inc_mut(n):
    """
    Mutative incrementation of a binary number in list format.
    Runtime analysis:
    n is proportional to the length of list_to_increment:
    Has O(n) runtime in the average and maximal case.
    The average case is still a lot faster than the maximal case because the program stops after realising that
    there is no point to continue adding since the carry is 0.
    This is a lot faster than the average case of the non-mutative implementation,
    because the rest of the list doesn't have to be copied.
    The minimal case is the runtime of O(1) when the first bit is 0,
    which is a much more common average case than the first implementation.
    Also, it doesn't get very much worse if it isn't because the bit after that could be 0.
    :param n: List to increment
    :return: n + 1
    """
    # Constant runtime
    i = 0
    # Maximally len(n) times. Stop when the "next" bit is 0.
    # The bit after that won't have to be incremented, since 1 + 0 = 0 + 1 = 1, with carry 0
    while i < len(n) and n[i] == 1:
        # Everything at this point has a constant runtime.
        n[i] = 0
        i = i + 1
    if i == len(n):
        n.append(1)
    else:
        n[i] = 1


# Task 3:
def benchmark(n):
    i = to_01list(0)

    def benchmark1():
        global d
        d = i
        # Iterate to bin(n) with non-mutative method.
        while d != to_01list(n):
            d = bin_inc(d)

    def benchmark2():
        global d
        d = i
        # Iterate to bin(n) with mutative method.
        while d != to_01list(n):
            bin_inc_mut(d)

    # Do the stopwatching
    start = timeit.default_timer()
    benchmark1()
    end = timeit.default_timer()
    diff1 = end - start
    start = timeit.default_timer()
    benchmark2()
    end = timeit.default_timer()
    diff2 = end - start

    # Print the timings
    print(str(n) + "\t" + str(diff1) + "\t" + str(diff2))


# Run the benchmark up to 100000.
# That means this will iterate from 0 to all numbers between 0 and 100000 with both methods.
for i in range(0, 100000, 1000):
    benchmark(i)


