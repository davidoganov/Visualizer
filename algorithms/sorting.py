"""
sorting.py

This module contains implementations of various sorting algorithms.
Each function will take a list and sort it in-place.

Algorithms to implement:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
"""

# Import necessary modules (if needed)


def bubble_sort(arr, capture_step=None):
    """Sorts an array using Bubble Sort algorithm, capturing each step for visualization."""
    n = len(arr)

    for i in range(n - 1):  # Loop over the array multiple times
        swapped = False
        for j in range(n - 1 - i):  # Reduce the range after each pass
            if arr[j] > arr[j + 1]:
                if capture_step:
                    capture_step(arr.copy(), j, j + 1)  # **Capture BEFORE swap**

                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True

        if not swapped:  # If no swaps occurred, exit early
            break

    # Final capture step to mark the sorted state
    if capture_step:
        capture_step(arr.copy(), None, None)  # Final state, no swaps


def selection_sort(arr):
    """Sorts an array using Selection Sort algorithm."""
    #     SELECTION_SORT(arr)
    # 1. Get the length of arr as n
    # 2. Repeat for each index i from 0 to n-1:
    #    3. Set min_index to i
    #    4. For each j from i+1 to n-1:
    #       5. If arr[j] < arr[min_index], update min_index to j
    #    6. Swap arr[i] and arr[min_index] (put the smallest value at position i)
    # 7. Return the sorted arr
    pass


def insertion_sort(arr):
    """Sorts an array using Insertion Sort algorithm."""
    #     INSERTION_SORT(arr)
    # 1. Get the length of arr as n
    # 2. Repeat for each index i from 1 to n-1:
    #    3. Set key = arr[i]
    #    4. Set j = i - 1
    #    5. While j >= 0 and arr[j] > key:
    #       6. Shift arr[j] to arr[j+1]
    #       7. Decrement j
    #    8. Insert key at arr[j+1]
    # 9. Return the sorted arr
    pass


def merge_sort(arr):
    """Sorts an array using Merge Sort algorithm."""
    #     MERGE_SORT(arr)
    # 1. If arr has only 1 element, return arr
    # 2. Find middle index: mid = len(arr) // 2
    # 3. Divide arr into left and right halves:
    #    - left_half = arr[0:mid]
    #    - right_half = arr[mid:]
    # 4. Recursively call MERGE_SORT(left_half) and MERGE_SORT(right_half)
    # 5. Merge the sorted halves:
    #    6. Initialize pointers i, j, k to 0
    #    7. While i < len(left_half) and j < len(right_half):
    #       8. If left_half[i] <= right_half[j], set arr[k] = left_half[i] and increment i
    #       9. Else, set arr[k] = right_half[j] and increment j
    #      10. Increment k
    #    11. Copy any remaining elements from left_half and right_half to arr
    # 12. Return the sorted arr
    pass


def quick_sort(arr):
    """Sorts an array using Quick Sort algorithm."""
    #    QUICK_SORT(arr)
    # 1. If arr has 1 or no elements, return arr
    # 2. Choose a pivot element (e.g., arr[len(arr) // 2])
    # 3. Partition arr into:
    #    - left (elements < pivot)
    #    - middle (elements == pivot)
    #    - right (elements > pivot)
    # 4. Recursively call QUICK_SORT(left) and QUICK_SORT(right)
    # 5. Concatenate sorted left, middle, and sorted right and return the result
    pass
