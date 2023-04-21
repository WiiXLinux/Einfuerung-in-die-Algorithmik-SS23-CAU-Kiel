# Best case: n = 0 => Q(1)
# Worst case: Q(log_2(n))
# Average case: Q(log_2(n))
'''
Runtime for the function to_bin() is O(log_2(n)), n being the value of the number put into the function. If the number
that is to be converted to binary has a value of 0 or 1, runtime is better compared to runtimes for higher values:
in case of 0 the function is called, fails the requirements for starting the while-loop. Hence it returns an empty string, 
which boils down to O(1). In case of 1, the while loop is called once, adding '1' to the result string, which then is
returned by to_bin(). Runtime in this case then is O(1) again. This is worse, if runtime is compared 
to the theoretical avg-runtime of O(log_2(n)), though it is quicker than any other input, because for any other higher 
number the while loop is called at least 2 times (for input 2).
There are no differences between Avg- and Worst-Case, these are both O(log_2(n)). Every time the while loop iterates, the
n gets halved, which means log_2(n) applies. 
'''
def to_bin(n):
    counter_of_operations = 0
    res = ""
    while n != 0:
        res = str(n % 2) + res
        n = n // 2
        counter_of_operations += 1
    print(counter_of_operations)
    return res


# Best case: n = 0 => Q(1)
# Worst case: Q(n)
# Average case: Q(n)
'''
One could argue, because strings are immutable, that the consistantly repeated loading of res within the for loop 
prolongs the runtime by constant factor 2 - constant factors are irrelevant for runtime approximations, so for ease of 
understanding we will only note this now, but not take into consideration for further discussion.
Runtime for function reverse() is O(n), n being the length of the string given to the function. 
There are no differences between Worst- and Average-Case because for any string, the for-loop is called exactly as 
many times as there are characters within the string. Best-Case is O(1), if the length of the string equals 0, in which
case the for-loop is called exactly once, returns an empty string and terminates after that.
'''
def reverse(s):
    counter_of_operations = 0
    res = ''
    for c in s:
        res = c + res
        counter_of_operations += 1
    print(counter_of_operations)
    return res

n = 15
print(n)
reverse(n*"1")

