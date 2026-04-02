"""
Randomized Quickselect Algorithm
-------------------------------
Finds k-th smallest element using random pivot.
Expected time complexity: O(n)
Worst-case: O(n^2)
"""

import random

def randomized_select(arr, k):
    """
    Returns k-th smallest element (0-based index)
    """

    if len(arr) == 1:
        return arr[0]

    # Random pivot selection
    pivot = random.choice(arr)

    # Partitioning
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(low):
        return randomized_select(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return randomized_select(high, k - len(low) - len(equal))