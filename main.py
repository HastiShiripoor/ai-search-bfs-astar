import os
import numpy as np
import heapq
from collections import deque
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost



class QueueEntry:
    # Priority-queue item for A*: ordered by f(n) = g(n) + h(n), exactly like the original Node.__lt__.
    def __init__(self, f, node):
        self.f = f
        self.node = node

    def __lt__(self, other):
        return self.f < other.f



# True  = BFS skips states that were already reached (no repeated nodes, always terminates).
# False = original behaviour (pure tree search, repeated states are expanded again).
BFS_AVOID_REPEATED_STATES = True


def tree_search(problem, fringe, expansion_order):
    fringe = deque(fringe)
    fringe.append(Node(problem.initial_state))
    reached = {problem.initial_state}
    
    while fringe:
        node = fringe.popleft()  # BFS
        expansion_order.append(problem.get_node_name(node.state))
        
        if problem.goal_test(node.state):
            return solution(node), expansion_order
        
        for child in expand(node, problem):
            if BFS_AVOID_REPEATED_STATES:
                if child.state in reached:
                    continue
                reached.add(child.state)
            fringe.append(child)
    
    return None, expansion_order




def expand(node, problem):
    successors = []
    for action, result in problem.successor_fn(node.state):
        g_cost = node.path_cost + problem.step_cost(node.state, action, result)
        successor = Node(result, parent=node, action=action, path_cost=g_cost) # ساخت گره فرزند
        successors.append(successor)
    return successors



def bfs(problem):
    expansion_order = []
    solution_path, expansion_order = tree_search(problem, [], expansion_order)
    return solution_path, expansion_order



def a_star(problem):
    fringe = []
    initial_node = Node(problem.initial_state)
    heapq.heappush(fringe, QueueEntry(problem.h_values[initial_node.state], initial_node))
    closed_set = set()  #گره‌های دیده شده
    expansion_order = []
    
    while fringe:
        node = heapq.heappop(fringe).node
        expansion_order.append(problem.get_node_name(node.state))
        
        if problem.goal_test(node.state):
            return solution(node), expansion_order
        
        closed_set.add(node.state)
        
        for successor in expand(node, problem):
            if successor.state not in closed_set:
                f_cost = successor.path_cost + problem.h_values[successor.state]
                heapq.heappush(fringe, QueueEntry(f_cost, successor))
    
    # print("No path found.")
    return None, expansion_order



def solution(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path





class Problem:
    def __init__(self, initial_state, h_values, adjacency_matrix, node_names):
        self.initial_state = initial_state
        self.h_values = h_values
        self.adjacency_matrix = adjacency_matrix
        self.node_names = node_names
        
        #وضعیت هدف
        goal_candidates = np.where(h_values == 0)[0]
        if len(goal_candidates) == 0:
            print("Error: No node with h(n) = 0 found. Please check your input.")
            exit()
        elif len(goal_candidates) == 1:
            self.goal_state = goal_candidates[0]
        else:
            print("Multiple nodes have h(n) = 0. Available goals:", ", ".join([node_names[i] for i in goal_candidates]))
            goal_node_name = input("Enter the name of your desired goal node: ")
            self.goal_state = np.where(node_names == goal_node_name)[0][0]
    
    def goal_test(self, state):
        return state == self.goal_state
    
    def successor_fn(self, state):
        successors = []
        index = state
        for i in range(len(self.adjacency_matrix)):
            if self.adjacency_matrix[index][i] > 0:
                successors.append((i, i))
        return successors

    def step_cost(self, state, action, result):
        return self.adjacency_matrix[state][result]
    
    def get_node_name(self, state):
        return self.node_names[state]




def is_directed_graph(adjacency_matrix):
    if np.array_equal(adjacency_matrix, adjacency_matrix.T):
        print("The graph is undirected.")
        user_response = input("The graph is undirected. Do you want to continue? (yes/no): ").strip().lower()
        if user_response != 'yes':
            print("Exiting as per user's request.")
            exit()
        else:
            print("Continuing execution with an undirected graph.")
    else:
        print("The graph is directed.")




def default_dir(*candidates):
    # Folder where the file dialog starts: a data folder next to this script if one exists.
    base = os.path.dirname(os.path.abspath(__file__))
    for name in candidates:
        path = os.path.join(base, name)
        if os.path.isdir(path):
            return path
    return base


def load_files():
    Tk().withdraw()
    
    print("Please select the adjacency matrix file (TXT format with commas as separators).")
    adjacency_matrix_path = askopenfilename(title="Select Adjacency Matrix TXT File", initialdir=default_dir(os.path.join("data", "adjacency_matrices"), "Adjacency_Matrix"))
    
    with open(adjacency_matrix_path, 'r') as file:
        lines = file.readlines()
        node_names = lines[0].strip().split(',')[1:]
        adjacency_matrix = np.array([list(map(int, line.strip().split(',')[1:])) for line in lines[1:]])
    
    print("Adjacency Matrix successfully loaded:")
    print(adjacency_matrix)
    
    print("\nPlease select the h values file (TXT format with commas as separators).")
    h_values_path = askopenfilename(title="Select H Values TXT File", initialdir=default_dir(os.path.join("data", "heuristics"), "H_Values"))
    
    with open(h_values_path, 'r') as file:
        lines = file.readlines()
        h_values = np.array(list(map(int, lines[1].strip().split(','))))
    
    print("H Values successfully loaded:")
    print(h_values)
    
    return adjacency_matrix, h_values, node_names





def draw_graph_with_path(problem, path, expansion_order, title):
    G = nx.DiGraph()
    
    #یال‌های گراف
    for i in range(len(problem.adjacency_matrix)):
        for j in range(len(problem.adjacency_matrix)):
            if problem.adjacency_matrix[i][j] > 0:
                G.add_edge(problem.node_names[i], problem.node_names[j], weight=problem.adjacency_matrix[i][j])
    
    pos = nx.spring_layout(G) #موقعیت گره‌ها
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=500)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if path:
        path_edges = [(problem.node_names[path[i]], problem.node_names[path[i + 1]]) for i in range(len(path) - 1)]
        nx.draw_networkx_nodes(G, pos, nodelist=[problem.get_node_name(state) for state in path], node_color='orange')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    nx.draw_networkx_nodes(G, pos, nodelist=expansion_order, node_color='yellow')
    
    plt.title(title)
    plt.show()


'''-----------------------------------------------------------------------------------------------------------------------------------------------------'''


adjacency_matrix, h_values, node_names = load_files()
node_names = np.array(node_names)
is_directed_graph(adjacency_matrix)

print("\nAvailable nodes:", ", ".join(node_names))
initial_node_name = input("Enter the name of the initial node from the options above: ")

initial_state = np.where(node_names == initial_node_name)[0]
if initial_state.size == 0:
    print(f"Error: Node name '{initial_node_name}' is not valid. Please run the program again and enter a valid node name.")
else:
    initial_state = initial_state[0]
    problem = Problem(initial_state, h_values, adjacency_matrix, node_names)
    goal_node_name = problem.get_node_name(problem.goal_state)
    print("\nThe goal node (determined by h(n) = 0) is:", goal_node_name)

    print("\nRunning Breadth-First Search (BFS)...")
    bfs_solution, bfs_expansion_order = bfs(problem)
    if bfs_solution:
        bfs_solution_names = [problem.get_node_name(state) for state in bfs_solution]
        print("BFS Solution Path:", " -> ".join(bfs_solution_names))
        print("BFS Expansion Order:", ", ".join(bfs_expansion_order))
        draw_graph_with_path(problem, bfs_solution, bfs_expansion_order, "BFS Solution and Expansion Order")
    else:
        print("No path found in BFS.")

    print("\nRunning A* Search...")
    a_star_solution, a_star_expansion_order = a_star(problem)
    if a_star_solution:
        a_star_solution_names = [problem.get_node_name(state) for state in a_star_solution]
        print("A* Solution Path:", " -> ".join(a_star_solution_names))
        print("A* Expansion Order:", ", ".join(a_star_expansion_order))
        draw_graph_with_path(problem, a_star_solution, a_star_expansion_order, "A* Solution and Expansion Order")
    else:
        print("No path found in A*.")
