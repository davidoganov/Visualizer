import tkinter as tk
from tkinter import ttk

def display_algorithm_summary_gui():
    """Displays the algorithm summary in a GUI window."""

    # Create the main window
    root = tk.Tk()
    root.title("Algorithm Summary")
    root.geometry("750x500")
    root.configure(bg="white")

    # Create a scrollable frame
    frame = tk.Frame(root, bg="white")
    canvas = tk.Canvas(frame, bg="white")
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Title
    title_label = tk.Label(scrollable_frame, text="📖 Algorithm Summary", font=("Arial", 18, "bold"), bg="white")
    title_label.pack(pady=10)

    # Big-O Notation Explanation
    big_o_label = tk.Label(scrollable_frame, text="Understanding Big-O Notation:", font=("Arial", 14, "bold"), bg="white")
    big_o_label.pack(anchor="w", padx=10)

    big_o_text = """Big-O notation describes how an algorithm's runtime grows as input size increases:
    
    - O(1): Constant Time - Fastest, independent of input size.
    - O(log n): Logarithmic Time - Example: Binary Search.
    - O(n): Linear Time - Example: Scanning an array.
    - O(n log n): Linearithmic Time - Example: Merge Sort.
    - O(n²): Quadratic Time - Example: Bubble Sort.
    - O(2ⁿ): Exponential Time - Extremely slow, e.g., recursive brute-force.
    - O(n!): Factorial Time - Used in brute-force problems like the Traveling Salesman Problem.
    """
    big_o_desc = tk.Label(scrollable_frame, text=big_o_text, font=("Arial", 12), justify="left", bg="white")
    big_o_desc.pack(anchor="w", padx=10, pady=5)

    # Algorithms Summary
    algo_label = tk.Label(scrollable_frame, text="Sorting & Searching Algorithms:", font=("Arial", 14, "bold"), bg="white")
    algo_label.pack(anchor="w", padx=10, pady=5)

    algorithms = {
        "Two-Pointer Search": "Uses two indices moving toward each other to find conditions efficiently.",
        "Binary Search": "Divides a sorted array and searches for an element in O(log n) time.",
        "Linear Search": "Scans each element in an array one-by-one (O(n) time complexity).",
        "Merge Sort": "Efficient O(n log n) sorting algorithm using divide-and-conquer.",
        "Bubble Sort": "Simple but slow sorting algorithm with O(n²) complexity.",
        "Quick Sort": "Picks a pivot, partitions elements, and sorts recursively (O(n log n) avg case).",
        "Insertion Sort": "Sorts elements one at a time, efficient for small datasets (O(n²)).",
        "BFS (Breadth-First Search)": "Explores nodes layer by layer in graphs (O(V+E) complexity).",
        "DFS (Depth-First Search)": "Explores as deep as possible before backtracking (O(V+E)).",
        "Dijkstra’s Algorithm": "Finds shortest paths in weighted graphs using a priority queue (O(V log V + E)).",
        "A* Algorithm": "Optimized pathfinding using heuristics, useful in AI and maps."
    }

    for name, desc in algorithms.items():
        algo_name = tk.Label(scrollable_frame, text=f"🔹 {name}", font=("Arial", 12, "bold"), bg="white")
        algo_name.pack(anchor="w", padx=20)
        algo_desc = tk.Label(scrollable_frame, text=desc, font=("Arial", 11), justify="left", bg="white")
        algo_desc.pack(anchor="w", padx=30)

    # Table Header
    table_label = tk.Label(scrollable_frame, text="Algorithm Complexity Table:", font=("Arial", 14, "bold"), bg="white")
    table_label.pack(anchor="w", padx=10, pady=10)

    # Table Data
    columns = ("Algorithm", "Best", "Average", "Worst", "Space", "Stable?")
    data = [
        ("Bubble Sort", "O(n)", "O(n²)", "O(n²)", "O(1)", "Yes"),
        ("Selection Sort", "O(n²)", "O(n²)", "O(n²)", "O(1)", "No"),
        ("Insertion Sort", "O(n)", "O(n²)", "O(n²)", "O(1)", "Yes"),
        ("Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "Yes"),
        ("Quick Sort", "O(n log n)", "O(n log n)", "O(n²)", "O(log n)", "No"),
        ("Linear Search", "O(1)", "O(n)", "O(n)", "O(1)", "Yes"),
        ("Binary Search", "O(1)", "O(log n)", "O(log n)", "O(1)", "No"),
        ("Two-Pointer", "O(n)", "O(n)", "O(n)", "O(1)", "Yes"),
        ("BFS", "O(V+E)", "O(V+E)", "O(V+E)", "O(V)", "Yes"),
        ("DFS", "O(V+E)", "O(V+E)", "O(V+E)", "O(V)", "No"),
        ("Dijkstra", "O(V log V)", "O(V log V + E)", "O(V log V + E)", "O(V+E)", "Yes"),
        ("A* Search", "O(b^d)", "O(b^d)", "O(b^d)", "O(b^d)", "Yes")
    ]

    table = ttk.Treeview(scrollable_frame, columns=columns, show="headings", height=12)
    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor="center", width=120)
    for row in data:
        table.insert("", "end", values=row)
    
    table.pack(padx=10, pady=10)

    # Run the GUI
    root.mainloop()
