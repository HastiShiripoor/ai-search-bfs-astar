# BFS and A* Graph Search Visualizer

A Python-based Artificial Intelligence course project that implements Breadth-First Search (BFS) and A* Search on a weighted graph loaded from text files. The program displays the solution path, node expansion order, and graph visualizations to help compare the behavior of the two search algorithms.

> **Course:** Artificial Intelligence  
> **University:** Urmia University of Technology  
> **Programming Language:** Python 3

## Overview

This project provides a visual and programmatic comparison of Breadth-First Search (BFS) and A* Search.

The user selects an adjacency matrix file and a heuristic-value file. The program loads the graph, asks the user to specify a starting node, and determines the goal node from the heuristic values. A node with a heuristic value of zero is considered a goal; if multiple nodes satisfy this condition, the user is prompted to choose one.

Both search algorithms are executed, and their solution paths and node expansion orders are displayed in the console. The graph is also visualized, with the solution path and expanded nodes highlighted.

## Features

- Loads weighted adjacency matrices from comma-separated text files.
- Loads heuristic values from text files.
- Detects whether the graph is directed or undirected.
- Identifies the goal node using the heuristic value `h(n) = 0`.
- Allows the user to select a starting node.
- Implements Breadth-First Search (BFS).
- Implements A* Search using the evaluation function `f(n) = g(n) + h(n)`.
- Displays solution paths and node expansion orders.
- Visualizes graphs using NetworkX and Matplotlib.
- Highlights solution paths and expanded nodes in graph visualizations.
- Supports file selection through Tkinter dialogs.

## Technologies Used

- Python 3
- NumPy
- NetworkX
- Matplotlib
- Tkinter
- `heapq`

## Project Structure

```text
ai-search-bfs-astar/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── docs/
│   ├── photo_1.png
│   └── photo_2.png
└── data/
    ├── adjacency_matrices/
    └── heuristics/
```

The `data/` directories are intended to contain adjacency matrix and heuristic input files. The actual directory structure may vary depending on the files included in the repository.

## Prerequisites

- Python 3.9 or later
- pip
- Tkinter support

Tkinter is commonly included with Python installations on Windows and macOS. On some Linux distributions, it may need to be installed separately.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/ai-search-bfs-astar.git
cd ai-search-bfs-astar
```

Replace `YOUR-USERNAME` with your GitHub username and adjust the repository name if necessary.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

If Tkinter is missing on Linux, install the appropriate system package for your distribution.

## Usage

Run the application from the project directory:

```bash
python main.py
```

Follow these steps:

1. Select an adjacency matrix text file.
2. Select the corresponding heuristic-value file.
3. Enter the starting node when prompted.
4. Review the BFS and A* solution paths and expansion orders in the console.
5. Inspect the generated graph visualizations. Close each plot window when you are ready to continue.

The adjacency matrix and heuristic files must refer to the same nodes in the same order.

## Input File Format

### Adjacency Matrix

The adjacency matrix is stored as comma-separated values. The first row contains node names, and the first column identifies the corresponding rows. A value of `0` represents the absence of an edge; nonzero values represent edge costs.

Example:

```csv
,A,B,C
A,0,1,4
B,0,0,2
C,0,0,0
```

This example represents a directed graph with the edges `A → B`, `A → C`, and `B → C`.

### Heuristic Values

The heuristic file contains two lines:

- Line 1: node names.
- Line 2: heuristic values in the corresponding order.

Example:

```csv
A,B,C
3,1,0
```

In this example, node `C` has a heuristic value of zero and can be identified as the goal node.

## Algorithms

### Breadth-First Search (BFS)

BFS explores the graph level by level using a FIFO queue. It is suitable for finding a path with the fewest edges when all edges are treated equally.

BFS does not use edge costs to prioritize nodes. Therefore, on a weighted graph, its solution is not necessarily the path with the lowest total cost.

### A* Search

A* uses a priority queue to select nodes according to the evaluation function:

`f(n) = g(n) + h(n)`

Where:

- `g(n)` is the accumulated cost from the starting node to node `n`.
- `h(n)` is the estimated cost from node `n` to the goal.
- `f(n)` is the estimated total cost of a solution through node `n`.

A* can find an optimal path when its implementation and heuristic satisfy the necessary conditions. For standard graph-search A*, heuristic admissibility and consistency, along with appropriate handling of improved paths, are important considerations.

## Results and Screenshots

The following screenshots show example executions of the program.

### BFS and A* Console Output

The first screenshot shows the loaded adjacency matrix and heuristic values, the selected start and goal nodes, the reported solution paths, and the expansion orders for both algorithms.

![BFS and A* console output and graph visualization](docs/bfs-result.png)

For the displayed example, the reported results are:

| Metric | BFS | A* |
|---|---|---|
| Start node | A | A |
| Goal node | G | G |
| Solution path | A → B → D → G | A → B → E → G |
| Expansion order | A, B, C, D, E, F, G | A, B, E, G |

### BFS Graph Visualization

The second screenshot shows the graph visualization for the BFS execution, including the highlighted solution path.

![BFS graph visualization](docs/bfs-graph.png)

These results describe the specific input and execution shown in the screenshots. They are examples rather than guarantees for every graph.

## Limitations

- BFS prioritizes the number of edges rather than their costs, so it does not generally minimize the total cost on weighted graphs.
- A* optimality depends on the heuristic and the correctness of the search implementation.
- A heuristic value of zero is used to identify a goal node. If multiple nodes have a value of zero, the program may require the user to select the intended goal.
- Input validation depends on the implementation. Invalid files, mismatched node orders, or malformed values may cause errors if they are not handled explicitly.
- The behavior of repeated-state handling in BFS depends on the configuration and implementation in `main.py`.

## Future Improvements

- Add comprehensive input-file validation.
- Validate that adjacency matrix and heuristic files use matching node names and ordering.
- Add command-line arguments for selecting input files.
- Add Uniform-Cost Search and Greedy Best-First Search for comparison.
- Add automated unit tests for graph loading and search algorithms.
- Improve visualization labels and provide a clearer comparison of path costs and expansion orders.

## License and Academic Attribution

This repository contains coursework developed for an Artificial Intelligence course at Urmia University of Technology.

No license is specified in this README. If the project is to be distributed publicly, add an appropriate license after deciding how the code may be reused.

Any third-party datasets or externally sourced graph examples should be credited to their original sources. Add the source of the Romania road-map dataset here only if that dataset is actually included in the repository and its origin has been verified.
