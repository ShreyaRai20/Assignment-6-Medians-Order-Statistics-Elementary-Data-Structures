import random

# =========================
# Deterministic Selection
# =========================
def deterministic_select(arr, k):
    """
    Deterministic selection (Median of Medians) algorithm.
    Returns the k-th smallest element in an array.
    
    Parameters:
    arr (list): input list of numbers
    k (int): order statistic to find (1-indexed)
    
    Returns:
    int/float: k-th smallest element in arr
    """

    # Base case: if array is small, sort and return directly
    if len(arr) <= 5:
        return sorted(arr)[k-1]

    # Step 1: divide array into groups of 5
    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]

    # Step 2: find the median of each group
    medians = [sorted(group)[len(group)//2] for group in groups]

    # Step 3: find pivot (median of medians)
    pivot = deterministic_select(medians, len(medians)//2 + 1)

    # Step 4: partition array into elements < pivot and > pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    count = arr.count(pivot)  # count of pivot in array

    # Step 5: recursively find the k-th smallest
    if k <= len(low):
        return deterministic_select(low, k)
    elif k > len(low) + count:
        return deterministic_select(high, k - len(low) - count)
    else:
        return pivot  # pivot is the k-th element

# =========================
# Randomized Selection
# =========================
def randomized_select(arr, k):
    """
    Randomized Quickselect algorithm.
    Returns the k-th smallest element in an array (1-indexed).
    
    Parameters:
    arr (list): input list of numbers
    k (int): order statistic (1-indexed)
    
    Returns:
    int/float: k-th smallest element
    """

    # Base case: only one element
    if len(arr) == 1:
        return arr[0]

    # Randomly choose pivot
    pivot = random.choice(arr)

    # Partition the array
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    count = arr.count(pivot)

    # Recurse into the correct partition
    if k <= len(low):
        return randomized_select(low, k)
    elif k > len(low) + count:
        return randomized_select(high, k - len(low) - count)
    else:
        return pivot

# =========================
# Example Usage
# =========================
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26, 3, 12, 7]
    k = 5
    print("Array:", arr)
    print(f"{k}-th smallest (Deterministic):", deterministic_select(arr, k))
    print(f"{k}-th smallest (Randomized):", randomized_select(arr, k))