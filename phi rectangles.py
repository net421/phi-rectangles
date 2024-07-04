import matplotlib.pyplot as plt
import numpy as np

def fibonacci_sequence(n):
    fib_seq = [0, 1]  # Starting from 0, 1 as per the Fibonacci sequence
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def draw_square(size, color):
    # Draw a square
    plt.plot([0, size, size, 0, 0], [0, 0, size, size, 0], color)

if __name__ == "__main__":
    n = 13 # Number of squares to generate (adjust as needed)
    sizes = fibonacci_sequence(n)
    colors = plt.cm.viridis(np.linspace(0, 1, n))  # Generate n different colors
    plt.figure(figsize=(3 * n, 3))  # Set the figure size
    for i, (size, color) in enumerate(zip(sizes, colors)):
        ax = plt.subplot(1, n, i+1)
        draw_square(size, color)
        ax.set_title(f"Size: {size} inches")
        ax.set_xlim(-0.1, max(sizes) + 0.1)  # Set x-axis limits to ensure correct scaling
        ax.set_ylim(-0.1, max(sizes) + 0.1)  # Set y-axis limits to ensure correct scaling
        ax.axis('off')  # Turn off axis
    plt.show()