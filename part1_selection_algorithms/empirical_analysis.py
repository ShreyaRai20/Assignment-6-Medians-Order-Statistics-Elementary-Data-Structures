"""
Empirical Analysis comparing Deterministic vs Randomized Selection Algorithms
This script measures and visualizes the execution time of two selection algorithms:
1. Deterministic selection using Median of Medians (select)
2. Randomized selection using Quickselect (randomized_select)

It generates a graph of execution time vs input size, which helps analyze practical
performance differences between these algorithms.
"""

import random  # For generating random input arrays
import time    # For measuring execution time
import matplotlib.pyplot as plt  # For plotting graphs

# Import your deterministic and randomized selection implementations
from deterministic_selection import select
from randomized_selection import randomized_select


def run_experiment(n):
    """
    Run one experiment for input size n.
    
    Parameters:
        n (int): Size of the array to generate and run the algorithms on.
        
    Returns:
        tuple: (deterministic_time, randomized_time)
    """
    # Generate a random array of size n with integers between 1 and 10000
    arr = [random.randint(1, 10000) for _ in range(n)]
    
    # Choose k as the median index (n // 2) for selection
    k = n // 2

    # -----------------------------
    # Deterministic Selection
    # -----------------------------
    # Record start time
    start = time.time()
    
    # Run the deterministic selection algorithm
    select(arr.copy(), k)  # Use arr.copy() to avoid modifying the original array
    
    # Calculate elapsed time
    deterministic_time = time.time() - start

    # -----------------------------
    # Randomized Selection
    # -----------------------------
    # Record start time
    start = time.time()
    
    # Run the randomized selection algorithm
    randomized_select(arr.copy(), k)
    
    # Calculate elapsed time
    randomized_time = time.time() - start

    # Return both execution times
    return deterministic_time, randomized_time


if __name__ == "__main__":
    # Define the input sizes we want to test
    sizes = [100, 500, 1000, 5000, 10000, 20000]  # Can extend for larger inputs

    # Lists to store execution times for each algorithm
    deterministic_times = []
    randomized_times = []

    # Run experiments for each input size
    for n in sizes:
        d_time, r_time = run_experiment(n)
        
        # Store the measured times
        deterministic_times.append(d_time)
        randomized_times.append(r_time)
        
        # Print execution times to console
        print(f"Size: {n} | Deterministic: {d_time:.6f}s | Randomized: {r_time:.6f}s")

    # -----------------------------
    # Plotting the results
    # -----------------------------
    # Create a figure with size 10x6 inches
    plt.figure(figsize=(10, 6))
    
    # Plot deterministic times with circles as markers
    plt.plot(sizes, deterministic_times, marker='o', label='Deterministic (Median of Medians)')
    
    # Plot randomized times with squares as markers
    plt.plot(sizes, randomized_times, marker='s', label='Randomized (Quickselect)')
    
    # Add a title to the graph
    plt.title('Selection Algorithm Performance: Deterministic vs Randomized')
    
    # Label the x-axis and y-axis
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    
    # Add a legend to differentiate the two algorithms
    plt.legend()
    
    # Enable grid for easier visualization
    plt.grid(True)
    
    # Adjust layout to prevent clipping of labels
    plt.tight_layout()
    
    # Save the graph as a PNG file
    plt.savefig("selection_algorithms_comparison.png")
    
    # Display the graph
    plt.show()