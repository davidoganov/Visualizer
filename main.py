"""
main.py

Entry point for the Algorithm Visualizer.

This script allows users to choose from different algorithm visualizations
and runs the corresponding Matplotlib-based visualization.

Options:
- Sorting Algorithms
- Pathfinding Algorithms
- Searching Algorithms
"""

import sys

from visualizer.sorting_visualizer import visualize_sorting
from visualizer.pathfinding_visualizer import visualize_pathfinding
from visualizer.searching_visualizer import visualize_search

import random
import string

list_numbers = [
    random.choice(
        [
            random.randint(-100, 100),
            random.uniform(-100, 100),
            complex(random.uniform(-100, 100), random.uniform(-100, 100)),
        ]
    )
    for _ in range(10)
]
list_letters = [random.choice(string.ascii_letters) for _ in range(10)]
list_words = ["".join(random.choices(string.ascii_lowercase, k=5)) for _ in range(5)]


def display_menu():
    """Displays the main menu options for the algorithm visualizer."""
    print("\n📌 Algorithm Visualizer Menu")
    print("1️⃣ - Sorting Algorithms")
    print("2️⃣ - Pathfinding Algorithms")
    print("3️⃣ - Searching Algorithms")
    print("0️⃣ - Exit")


def main():
    """Main function to handle user selection and run visualizations."""
    while True:
        display_menu()
        choice = input("\nEnter the number of the algorithm category to visualize: ")

        if choice == "1":
            print("\n▶ Running Sorting Visualizer...")
            visualize_sorting()
        elif choice == "2":
            print("\n▶ Running Pathfinding Visualizer...")
            visualize_pathfinding()
        elif choice == "3":
            print("\n▶ Running Searching Visualizer...")
            visualize_search()
        elif choice == "0":
            print("\n👋 Exiting the Algorithm Visualizer. Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid choice. Please enter a valid number.")


if __name__ == "__main__":
    main()
