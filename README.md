# BFS and A* Graph Search Visualizer

A Python program for an Artificial Intelligence course project that runs **Breadth-First Search (BFS)** and **A\* Search** on a weighted graph loaded from text files, then visualizes the solution path and node expansion order.

> **Course:** `<AI>` · **University:** `<Urmia Technology>` · **Semester:** `<term5>`

## Overview

The user selects an adjacency matrix file and a heuristic (h-value) file. The program reads the graph, asks for a start node, takes the goal as the node whose heuristic value is `0`, and runs both algorithms so their results can be compared.

## Features

- Loads a weighted adjacency matrix and heuristic values from comma-separated `.txt` files
- Detects whether the graph is directed or undirected
- Identifies the goal node automatically (`h(n) = 0`); if several nodes qualify, asks the user to choose
- Runs BFS (tree search, FIFO queue) and A* (priority queue with a closed set, `f(n) = g(n) + h(n)`)
- Prints the solution path and the node expansion order for each algorithm
- Draws the graph with NetworkX/Matplotlib, highlighting the solution path and expanded nodes
- Includes 8 small sample graphs and a Romania road-map dataset

## Tech Stack

Python 3 · NumPy · NetworkX · Matplotlib · Tkinter (file-selection dialogs) · `heapq`

## Project Structure

```
ai-search-bfs-astar/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
    ├── adjacency_matrices/   # Adjacency Matrix _ 01..08.txt, Romania maps
    └── heuristics/           # H_Values_01..08.txt, Romania heuristics
```

> Adjust this tree to match your final layout.

## Prerequisites

- Python 3.9+ (Tkinter is included with the standard Windows/macOS installers; on some Linux distributions install `python3-tk`)

## Installation

```bash
git clone https://github.com/<your-username>/ai-search-bfs-astar.git
cd ai-search-bfs-astar
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

1. Select an adjacency matrix file from `data/adjacency_matrices/`.
2. Select the matching heuristic file from `data/heuristics/` (same node set and order).
3. Type the name of the start node when prompted.
4. Read the printed paths and expansion orders; close each plot window to continue.

> The file dialogs open in the project's `data/` folders when they exist; you can browse to any other folder from the dialog.

## Input File Format

**Adjacency matrix** (CSV; first row and first column are node names; `0` means no edge):

```
,A,B,C
A,0,1,4
B,0,0,2
C,0,0,0
```

**Heuristic file** (line 1 = node names, line 2 = h-values in the same order):

```
A,B,C
3,1,0
```

## Algorithms

| Algorithm | Frontier | Duplicate handling | Uses edge costs |
|-----------|----------|--------------------|-----------------|
| BFS | FIFO queue | reached-set (optional, on by default) | no (minimizes depth) |
| A* | priority queue on `g + h` | closed set | yes |

## Results and Screenshots

`<Add real screenshots of the console output and plots here, e.g. docs/romania_astar.png>`

## Limitations

- Optimality of A* depends on the heuristic being admissible and consistent; the program does not check this.
- BFS skips already-reached states by default (switch `BFS_AVOID_REPEATED_STATES` in `main.py` to `False` for pure tree search, which can be very slow or never finish on graphs with cycles).
- Input files are not validated (e.g., matching node order between the two files).

## Future Improvements

- Validate input files and heuristic properties
- Add command-line arguments instead of fixed dialog folders
- Add Uniform-Cost Search and Greedy Best-First Search for comparison
- Add unit tests

## License and Academic Attribution

This repository contains coursework for `<course name>`. License: `<choose, e.g. MIT>`.
The Romania map data follows the classic example used in AI textbooks (`<cite your course material>`).
