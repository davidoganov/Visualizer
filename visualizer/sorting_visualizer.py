"""
sorting_visualizer.py

This module provides a visualization for sorting algorithms using Matplotlib.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from algorithms.sorting import bubble_sort  # Import sorting algorithms


def animate_sorting(arr, sorting_algorithm):
    """Animates the sorting process using a grid layout with clear swap highlighting and extra space on the right."""

    fig, ax = plt.subplots(figsize=(12, 3))  # Wider figure for more space
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, len(arr) + 1)  # **Extra space added on the right**
    ax.set_ylim(-1, 2)  # Single row layout

    # Initialize tiles representing array elements
    tiles = [ax.add_patch(plt.Rectangle((i, 0), 1, 1, color='gray', edgecolor='black')) for i in range(len(arr))]
    text_labels = [ax.text(i + 0.5, 0.5, str(arr[i]), ha='center', va='center', fontsize=12, color='white') for i in range(len(arr))]

    frames = []  # Stores snapshots of the sorting process
    swap_indices = []  # Stores which indices are being swapped at each step

    def capture_sorting_state(state, index1=None, index2=None):
        """Captures sorting state at each step, marking swaps in blue."""
        frames.append(state.copy())
        swap_indices.append((index1, index2))  # Save swap indices for color updates

    sorting_algorithm(arr.copy(), capture_sorting_state)  # Run sorting with step capturing

    def update(frame_idx):
        """Updates visualization per sorting step, highlighting swaps."""
        if frame_idx < len(frames):
            snapshot = frames[frame_idx]
            index1, index2 = swap_indices[frame_idx]  # Get swap indices

            for i in range(len(snapshot)):
                tiles[i].set_xy((i, 0))  # Position the tile
                text_labels[i].set_position((i + 0.5, 0.5))  # Position text
                text_labels[i].set_text(str(snapshot[i]))  # Update number

                # Color coding:
                if index1 is not None and index2 is not None:
                    if i == index1 or i == index2:
                        tiles[i].set_color('blue')  # **Blue for swaps**
                    else:
                        tiles[i].set_color('gray')  # Default color
                else:
                    tiles[i].set_color('gray')  # Reset color when no swaps occur

        # Ensure previous swap colors reset AFTER one frame delay
        if frame_idx > 0:
            prev_index1, prev_index2 = swap_indices[frame_idx - 1]
            if prev_index1 is not None and prev_index2 is not None:
                tiles[prev_index1].set_color('gray')  # Reset previous swap
                tiles[prev_index2].set_color('gray')  # Reset previous swap

        # If it's the last frame, mark all elements as sorted (Green)
        if frame_idx == len(frames) - 1:
            for tile in tiles:
                tile.set_color('green')  # Green for final sorted array

    # **Slower animation speed for better visibility (700ms per frame)**
    ani = animation.FuncAnimation(fig, update, frames=len(frames), repeat=False, interval=700)
    plt.show()


def get_sorting_choice():
    """Displays the sorting algorithm menu and gets user input."""
    print("\n🔢 Sorting Algorithm Visualizer")
    print("📌 Available Sorting Algorithms:")
    print("1️⃣ - Bubble Sort")
    print("2️⃣ - Selection Sort (Coming Soon)")
    print("3️⃣ - Insertion Sort (Coming Soon)")
    print("4️⃣ - Merge Sort (Coming Soon)")
    print("5️⃣ - Quick Sort (Coming Soon)")
    print("0️⃣ - Back to Main Menu")

    return input("\nEnter choice (0-5): ")


def visualize_sorting():
    """Runs the sorting visualization based on user selection."""

    while True:  # Keep the sorting menu open until a valid choice is made
        sorting_choice = get_sorting_choice()

        sorting_algorithms = {
            "1": bubble_sort,
            "2": None,  # selection_sort (To be implemented)
            "3": None,  # insertion_sort (To be implemented)
            "4": None,  # merge_sort (To be implemented)
            "5": None,  # quick_sort (To be implemented)
        }

        if sorting_choice == "0":
            return  # Go back to the main menu

        if sorting_choice in sorting_algorithms:
            selected_algorithm = sorting_algorithms[sorting_choice]
            if selected_algorithm:
                arr = [
                    random.randint(1, 100) for _ in range(10)
                ]  # Generate a random array
                print(
                    f"\n▶ Running {selected_algorithm.__name__.replace('_', ' ').title()} Visualization..."
                )
                animate_sorting(arr, selected_algorithm)
                return  # Exit loop after running animation
            else:
                print(
                    "\n❌ This sorting algorithm is not implemented yet. Please choose another option."
                )
        else:
            print("\n❌ Invalid choice. Please enter a valid number.")


if __name__ == "__main__":
    visualize_sorting()
