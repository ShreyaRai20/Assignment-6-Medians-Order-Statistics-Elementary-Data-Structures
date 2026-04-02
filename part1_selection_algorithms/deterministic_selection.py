"""
Deterministic Selection Algorithm (Median of Medians)
----------------------------------------------------
This algorithm finds the k-th smallest element in O(n) worst-case time.

Steps:
1. Divide array into groups of 5
2. Find medians of each group
3. Recursively find median of medians
4. Use it as pivot and partition
5. Recurse on required side
"""

def insertion_sort(arr):
    """Helper function to sort small arrays (size <= 5)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def select(arr, k):
    """
    Returns the k-th smallest element (0-based index)
    """

    # Base case
    if len(arr) <= 5:
        return insertion_sort(arr)[k]

    # Step 1: Divide into groups of 5
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Step 2: Find medians of groups
    medians = [insertion_sort(group)[len(group)//2] for group in groups]

    # Step 3: Find pivot (median of medians)
    pivot = select(medians, len(medians)//2)

    # Step 4: Partition
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    # Step 5: Recurse
    if k < len(low):
        return select(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return select(high, k - len(low) - len(equal))