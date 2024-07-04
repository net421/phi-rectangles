Fibonacci Squares Visualization
This project visualizes squares with side lengths following the Fibonacci sequence. Each square is displayed in a different color, providing a unique visual representation of the Fibonacci sequence.

Requirements
Python 3.x
Matplotlib
Numpy
Installation
Clone the repository:

bash
Copiar código
git clone https://github.com/yourusername/fibonacci-squares-visualization.git
cd fibonacci-squares-visualization
Install the required packages:

bash
Copiar código
pip install matplotlib numpy
Usage
Run the script:

bash
Copiar código
python fibonacci_squares.py
The script will generate a plot with squares based on the Fibonacci sequence.

Code Explanation
The script consists of the following main components:

fibonacci_sequence(n): Generates a list of the first n Fibonacci numbers.
draw_square(size, color): Draws a square of a given size and color using matplotlib.
Main block: Generates and plots the squares based on the Fibonacci sequence.
Example
Here is a simplified version of the script:

python
Copiar código
import matplotlib.pyplot as plt
import numpy as np

def fibonacci_sequence(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def draw_square(size, color):
    plt.plot([0, size, size, 0, 0], [0, 0, size, size, 0], color)

if __name__ == "__main__":
    n = 10
    sizes = fibonacci_sequence(n)
    colors = plt.cm.viridis(np.linspace(0, 1, n))
    plt.figure(figsize=(3 * n, 3))
    for i, (size, color) in enumerate(zip(sizes, colors)):
        ax = plt.subplot(1, n, i+1)
        draw_square(size, color)
        ax.set_title(f"Size: {size} inches")
        ax.set_xlim(-0.1, max(sizes) + 0.1)
        ax.set_ylim(-0.1, max(sizes) + 0.1)
        ax.axis('off')
    plt.show()
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Feel free to submit issues, fork the repository and send pull requests.
