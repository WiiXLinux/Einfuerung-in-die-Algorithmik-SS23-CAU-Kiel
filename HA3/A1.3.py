import gc
import timeit

import OLD
import NEW

# We'll disable garbage collection to make the calculation results appear faster.
gc.disable()


def timeDiff(what_to_do, args, how_often):
    """
    Runs what_to_do how_often times and returns the last object of what_to_do returning and the time difference between
    the first execution of what_to_do starting and the last execution ending.
    :param what_to_do: Method that should be called
    :param args: Argument of the method, if None is given, timeDiff will execute what_to_do() and not what_to_do(args)
    :param how_often: How often should the method be executed
    :return: last object and delay as a tuple
    """
    if args is None:
        # Measure starting time
        start_time = timeit.default_timer()
        # Repeat what_to_do, how_often times.
        for i in range(0, how_often):
            o = what_to_do()
        # Set the difference between before and after the execution.
        d = timeit.default_timer() - start_time
        # Return the last object returned by what_to_do() and the time difference.
        return o, d

    # Measure starting time
    start_time = timeit.default_timer()
    # Repeat what_to_do, how_often times.
    for i in range(0, how_often):
        o = what_to_do(args)
    # Set the difference between before and after the execution.
    d = timeit.default_timer() - start_time
    # Return the last object returned by what_to_do(args) and the time difference.
    return o, d


print("Test 1: Initialisation of object")
q1, dt1 = timeDiff(OLD.Queue, None, 1)
q2, dt2 = timeDiff(NEW.Queue, None, 1)

print("New method faster than old method:", dt1 > dt2, "\nTime difference difference being: " + str(dt1-dt2)+ "s\n")

print("Test 2: Enqueueing many objects")
dt1 = timeDiff(q1.enqueue, [42], 1000000)[1]
dt2 = timeDiff(q2.enqueue, [42], 1000000)[1]

print("New method faster than old method:", dt1 > dt2, "\nTime difference difference being: " + str(dt1-dt2)+ "s\n")

print("Test 3: Dequeueing many objects")
dt1 = timeDiff(q1.dequeue, None, 1000)[1]
dt2 = timeDiff(q2.dequeue, None, 1000)[1]

print("New method faster than old method:", dt1 > dt2, "\nTime difference difference being: " + str(dt1-dt2)+ "s\n")

# Reset q1 and q2
q1 = OLD.Queue()
q2 = NEW.Queue()


print("Test 4: Enqueueing a big object")
dt1 = timeDiff(q1.enqueue, 1000000000 * [42], 1)[1]
dt2 = timeDiff(q2.enqueue, 1000000000 * [42], 1)[1]

print("New method faster than old method:", dt1 > dt2, "\nTime difference difference being: " + str(dt1-dt2)+ "s\n")

print("Test 5: Dequeueing the big object")
dt1 = timeDiff(q1.dequeue, None, 1)[1]
dt2 = timeDiff(q2.dequeue, None, 1)[1]

print("New method faster than old method:", dt1 > dt2, "\nTime difference difference being: " + str(dt1-dt2)+ "s\n")


print("Collecting Garbage")
gc.collect()
print("Exiting (Will take a bit to free the big queue objects in ram)")
