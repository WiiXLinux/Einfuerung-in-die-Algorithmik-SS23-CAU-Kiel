# Best case: n = 0 => Q(1)
# Worst case: Q(log_2(n))
# Average case: Q(log_2(n))

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

