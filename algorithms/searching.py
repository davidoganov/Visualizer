"""
searching.py

This module contains implementations of searching algorithms.
Algorithms to implement:
- Linear Search
- Binary Search
- Two Pointers Technique
"""

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

def two_pointer_method(arr, target):
    """Performs a search using the two pointer method to find the target in the array"""
    # TODO finish this function
    pass 

