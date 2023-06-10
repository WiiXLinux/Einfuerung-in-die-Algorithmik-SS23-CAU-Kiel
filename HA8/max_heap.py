# Copy of "heap (1).py" from the lecture, modified to use max-heaps and not min-heaps


import random


class Heap:

    def __init__(self):
        """
        construct an empty heap
        """
        self.heap = []

    def __heapify_up(self, i):
        """
        auxiliary function performing heapify_up at the given position i
        """
        parent_pos = (i - 1) // 2
        if i > 0 and self.heap[i] > self.heap[parent_pos]:
            # swap(self.heap, i, parent_pos)
            self.heap[i], self.heap[parent_pos] = \
                self.heap[parent_pos], self.heap[i]
            self.__heapify_up(parent_pos)

    def __heapify_down(self, i):
        """
        auxiliary function performing heapify_down at the given position i
        """
        left = i * 2 + 1
        right = left + 1
        cont = True
        # test with right, since we know
        # that both subtrees exist in loop body
        while cont and right < len(self.heap):
            if self.heap[left] > self.heap[right]:
                max_pos = left
            else:
                max_pos = right
            if self.heap[i] < self.heap[max_pos]:
                # swap(self.heap, i, min_pos)
                self.heap[i], self.heap[max_pos] = \
                    self.heap[max_pos], self.heap[i]
                i = max_pos
                left = i * 2 + 1
                right = left + 1
            else:
                cont = False

        if cont and left < len(self.heap):
            if self.heap[i] < self.heap[left]:
                # swap(self.heap, i, left)
                self.heap[i], self.heap[left] = \
                    self.heap[left], self.heap[i]

    @staticmethod
    def list_to_heap(l):
        """
        statical method to construct a heap containing all elements of the list
        efficient implementation with runtime O(len(l)).
        copy given list once, to avoid interference of the data structures.
        """
        h = Heap()
        h.heap = list(l)
        for i in range((len(h.heap) // 2) - 1, -1, -1):
            h.__heapify_down(i)
        return h

    def add(self, v):
        """
        add v to the given heap
        """
        self.heap.append(v)  # constant runtime
        self.__heapify_up(len(self.heap) - 1)

    def get_max(self):
        """
        return minimum value of the given heap
        """
        return self.heap[0]

    def extract_max(self):
        """
        extract the minimum value from the given heap and return it
        if the heap is empty, return None
        """
        if not self.heap:
            return None
        elif len(self.heap) == 1:
            max = self.heap[0]
            self.heap = []
            return min
        else:
            max = self.heap[0]
            self.heap[0] = self.heap.pop()  # important, since
            # constant runtime
            self.__heapify_down(0)
            return max

    def __str__(self):
        """
        return a tree-like representation of the given heap
        """

        def str_h(i):
            if i < len(self.heap):
                left_res = str_h(i * 2 + 1)
                right_res = str_h(i * 2 + 2)
                return ('(' + left_res + ',' + str(self.heap[i]) +
                        ',' + right_res + ')')
            else:
                return ''

        return str_h(0)


def rand_list(n):
    """
    produce random ist of numbers 0 to n-1.
    """
    res = list(range(n))
    for i in range(2 * n):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        res[i], res[j] = res[j], res[i]
    return res



