"""
searching_visualizer.py

This module provides a visualization for searching algorithms using Matplotlib.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from algorithms.searching import linear_search, binary_search  # Import algorithms


def animate_linear_search(arr, target):
    """Animates the Linear Search process step by step."""
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, len(arr))
    ax.set_ylim(-1, 1)

    rects = [
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color="gray", edgecolor="black"))
        for i in range(len(arr))
    ]
    text_labels = [
        ax.text(
            i + 0.5,
            0.5,
            str(arr[i]),
            ha="center",
            va="center",
            fontsize=12,
            color="white",
        )
        for i in range(len(arr))
    ]

    # Track search steps
    search_steps = []
    found_index = None

    # Record search steps
    for i in range(len(arr)):
        search_steps.append(i)
        if arr[i] == target:
            found_index = i
            break  # Stop after finding target

    def update(frame):
        """Updates visualization at each search step."""
        if frame < len(search_steps):
            i = search_steps[frame]
            rects[i].set_facecolor("blue")  # Highlight current checked element
            if i == found_index:
                rects[i].set_facecolor("green")  # Target found, highlight green
                ani.event_source.stop()  # Stop animation immediately
        return rects

    ani = animation.FuncAnimation(
        fig, update, frames=len(search_steps), repeat=False, interval=500
    )
    plt.title(f"Linear Search for {target}")
    plt.show()


def animate_binary_search(arr, target):
    """Animates the Binary Search process step by step."""
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, len(arr))
    ax.set_ylim(-1, 1)

    rects = [
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color="gray", edgecolor="black"))
        for i in range(len(arr))
    ]
    text_labels = [
        ax.text(
            i + 0.5,
            0.5,
            str(arr[i]),
            ha="center",
            va="center",
            fontsize=12,
            color="white",
        )
        for i in range(len(arr))
    ]

    search_steps = []
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        search_steps.append(mid)
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    def update(frame):
        """Updates visualization at each search step."""
        if frame < len(search_steps):
            mid = search_steps[frame]
            rects[mid].set_facecolor("blue")  # Highlight mid-point
            if arr[mid] == target:
                rects[mid].set_facecolor("green")  # If found, highlight green
                return
        return rects

    ani = animation.FuncAnimation(
        fig, update, frames=len(search_steps), repeat=False, interval=700
    )
    plt.title(f"Binary Search for {target}")
    plt.show()


def animate_two_pointer_search(arr, target):
    """Animates the Two-Pointer Search process step by step."""
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, len(arr))
    ax.set_ylim(-1, 1)

    # Draw array as squares
    rects = [
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color="gray", edgecolor="black"))
        for i in range(len(arr))
    ]
    text_labels = [
        ax.text(
            i + 0.5,
            0.5,
            str(arr[i]),
            ha="center",
            va="center",
            fontsize=12,
            color="white",
        )
        for i in range(len(arr))
    ]

    # Two-pointer search steps
    left, right = 0, len(arr) - 1
    search_steps = []

    while left < right:
        search_steps.append((left, right))  # Store pointer positions
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            break  # Stop at the first valid pair
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    def update(frame):
        """Updates visualization at each search step."""
        if frame < len(search_steps):
            l, r = search_steps[frame]

            # Reset all to gray before updating
            for rect in rects:
                rect.set_facecolor("gray")

            # Highlight current left and right pointers
            rects[l].set_facecolor("blue")
            rects[r].set_facecolor("blue")

            # If found, highlight green
            if arr[l] + arr[r] == target:
                rects[l].set_facecolor("green")
                rects[r].set_facecolor("green")
                ani.event_source.stop()  # Stop animation

        return rects

    ani = animation.FuncAnimation(
        fig, update, frames=len(search_steps), repeat=False, interval=700
    )
    plt.title(f"Two-Pointer Search for Pair Sum = {target}")
    plt.show()

def get_search_choice(arr, target):
    """Displays the search menu and gets user input."""
    print("\n🔍 Welcome to the Search Algorithm Visualizer!\n")
    print("📌 How this works:")
    print("   - The array is represented as small boxes.")
    print("   - Searching will be shown step by step with highlights.")
    print("   - Colors:")
    print("     🟦 Blue = Currently checking these elements.")
    print("     🟩 Green = Found the target match.")
    print("\nArray:", arr)
    print(f"Target to search for: {target}\n")

    print("➡ Choose a search algorithm:")
    print("1️⃣ - Linear Search (checks one by one)")
    print("2️⃣ - Binary Search (faster, cuts list in half each time)")
    print("3️⃣ - Two-Pointer Search (finds a pair summing to target)")

    return input("\nEnter choice (1, 2, or 3): ")


def visualize_search():
    """Runs the search visualization by handling user choice."""
    
    # Generate a sorted list for searching
    arr = sorted([random.randint(1, 100) for _ in range(15)])
    target = random.choice([arr[i] + arr[j] for i in range(len(arr)) for j in range(i+1, len(arr))] + [random.randint(101, 150)])

    # Get user's choice using the new function
    search_choice = get_search_choice(arr, target)

    # Run the selected search algorithm
    if search_choice == "1":
        print("\n▶ Running **Linear Search** Visualization...")
        animate_linear_search(arr, target)
    elif search_choice == "2":
        print("\n▶ Running **Binary Search** Visualization...")
        animate_binary_search(arr, target)
    elif search_choice == "3":
        print("\n▶ Running **Two-Pointer Search** Visualization...")
        animate_two_pointer_search(arr, target)
    else:
        print("❌ Invalid choice. Exiting search visualization.")


    print("\n🔍 Welcome to the Search Algorithm Visualizer!\n")
    print("📌 How this works:")
    print("   - The array is represented as small boxes.")
    print("   - Searching will be shown step by step with highlights.")
    print("   - Colors:")
    print("     🟦 Blue = Currently checking these elements.")
    print("     🟩 Green = Found the target match.")
    print("\nArray:", arr)
    print(f"Target to search for: {target}\n")

    # Ask the user to choose a search algorithm
    print("➡ Choose a search algorithm:")
    print("1️⃣ - Linear Search (checks one by one)")
    print("2️⃣ - Binary Search (faster, cuts list in half each time)")
    print("3️⃣ - Two-Pointer Search (finds a pair summing to target)")
    search_choice = input("\nEnter choice (1, 2, or 3): ")

    # Run the selected search algorithm
    if search_choice == "1":
        print("\n▶ Running **Linear Search** Visualization...")
        animate_linear_search(arr, target)
    elif search_choice == "2":
        print("\n▶ Running **Binary Search** Visualization...")
        animate_binary_search(arr, target)
    elif search_choice == "3":
        print("\n▶ Running **Two-Pointer Search** Visualization...")
        animate_two_pointer_search(arr, target)
    else:
        print("❌ Invalid choice. Exiting search visualization.")


if __name__ == "__main__":
    visualize_search()
