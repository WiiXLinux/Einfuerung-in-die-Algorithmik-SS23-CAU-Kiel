from max_heap import Heap

"""
Teilaufgabe 1:
Das Problem ließe sich leicht mit Laufzeit O(n · log(n)) lösen, indem man
einen beliebigen Algorithmus (der Laufzeit von O(n · log(n)) hat), wie zum
Beispiel Heapsort verwendet, um die Liste zu sortieren und dann einfach das
k-te Element zurückgibt.
Das Zugreifen auf das k-te Element hat konstante Laufzeit.
"""

"""
Teilaufgabe 2:
Ein ähnlicher Algorithmus ließe sich schneller Implementieren, indem man
statt wie in Heapsort alle Elemente des Heaps wieder extrahiert, einfach
genau k Mal die Elemente extrahiert und beim letzten Mal das Element
zurückgibt.
Die Laufzeitanalyse für diesen Algorithmus ist in seiner folgenden Implementierung.
"""


def k_largest_element(l: list[int], k: int) -> int:
    """
    Function that returns the kth largest element of a list l.

    Achieves that in average runtime of: O(n + k * log(n)).
    This runtime is a result of the combined runtime of Heap.list_to_heap(l) (runtime of O(n)) and
    repeating extract_max() (runtime of log(n)) exactly k times.

    The best case is runtime O(n) with k = 1 since we build the entire heap and then extract the top element.
    Adding these runtimes together results in the runtime O(n + log(n)) which is the same as O(n)

    The worst case is runtime O(n * log(n)) with k = n since we build the heap and then extract all the maxima.
    Equivalent to the runtime of heapsort.
    :param l: List to extract from
    :param k: Which kth maximum should be returned?
    :return: kth maximum of l
    """
    h = Heap.list_to_heap(l)  # Runtime of O(n)
    # Execute h.extract_max() exactly k - 1 times. -> O((k-1) * log(n))
    for i in range(k-1):
        h.extract_max()
    # Execute h.extract_max() exactly 1 time. -> O(1*log(n))
    return h.extract_max()


# Example
l = [3, 4, 1, 9, 2, 5]

print(k_largest_element(l, 4))
