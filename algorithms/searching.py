"""
searching.py

This module contains implementations of searching algorithms.
Algorithms to implement:
- Linear Search
- Binary Search
"""

# import random
# import string

# TODO Remove these functions
# Lists to be used in functions (located in main.py, here for reference)
# Random number list, random letters, and random words
# list_numbers = [
#     random.choice(
#         [
#             random.randint(-100, 100),
#             random.uniform(-100, 100),
#             complex(random.uniform(-100, 100), random.uniform(-100, 100)),
#         ]
#     )
#     for _ in range(10)
# ]
# list_letters = [random.choice(string.ascii_letters) for _ in range(10)]
# list_words = ["".join(random.choices(string.ascii_lowercase, k=5)) for _ in range(5)]


def linear_search(arr, target):
    """Performs Linear Search to find the target in the array."""
    sz = len(arr)
    for _ in range(sz):
        if arr[_] == target:
            return f"Target found at position: {_}"
    
    return "Target not found within arr"



def binary_search(arr, target):
    """Performs Binary Search to find the target in the array."""
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if (arr[mid] == target):
            return f"Target found at position: {mid}"
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    # target has not been found within the arr, left is at the insertion point
    return f"Target not found, should be inserted at position: {left}"

