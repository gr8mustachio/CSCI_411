import networkx as nx
import matplotlib.pyplot as plt
import math
from collections import deque
from queue import PriorityQueue
def euclidian(source, dest):
    """The Euclidian Distance Formula is used to find the distance between two points
    This function takes in two coords with format [x,y] and returns the Euclidian distance between the two points
    Returns:
        _type_: float
    """
    distance = (math.sqrt((dest[0] - source[0])**2 + (dest[1] - source[1])**2))
    return distance

def manhattan(source, dest):
    """Manhattan Distance Formula is isued to calculate the manhattan distance from two point
    Args:
        source (list): [x1, y1]
        dest (list): [x2, y2]]
    Returns:
        _type_: int
    """
    distance = abs(source[0] - dest[0]) + abs(source[1] - dest[1])
    return distance

def g(G, start, current):
    """Calculates cost of the path from the start node to n
    Args:
        start (tuple): a tuple of the4 starting node's (x,y) coords
        n (tuple): tuple of the current nodes (x,y) coords
    Returns:
        int: cost of path from start node to n
    """
    return nx.shortest_path_length(G, start, current, weight='weight')

                        


def a_star(G, source, dest):
    """Graph algorithm that uses heuristics to quickly determine a path from
       source to dest. 
    Args:
        G (networkx.classes.graph.Graph): A networkx graph
        source (tuple): our start position
        dest (tuple): our goal
    Returns:
        list: list of nodes on the path from source to dest
    """
    open = PriorityQueue() # contains visited nodes that have not yet been expanded
    inOpen = set() # set to keep track of nodes in priority queue, since we can't check the queue itself to see if it contains an object
    closed = set()
    gScore = {}
    hScore = {}
    gScore[source] = 0
    hScore[source] = gScore[source] + euclidian(source, dest)
    open.put((0, source))
    inOpen.add(source)
    parents = {}
    path = []
    parents[source] = source
    prev = source
    while open.empty() == False:
        neighborList = list(G.neighbors(prev))
        pass
        if open.queue[0] not in neighborList and prev != source:
            throwaway= open.get()
        current = open.get()
        current = current[1]
        inOpen.discard(current)
        gScore[current] = g(G, source, current)
        if current not in path:
            path.append(current)
        if current == dest:
            print("FOUND")
            print(path)
            return True
        else:
            for neighbor in G.neighbors(current):
                neighbors = list(G.neighbors(current))
                neighbor_cost = gScore[current] + G.get_edge_data(current, neighbor).get('weight')
                gScore[neighbor] = g(G, source, neighbor)
                if neighbor in inOpen:
                    if gScore[neighbor] <= neighbor_cost:
                        continue
                elif neighbor in closed:
                    if gScore[neighbor] <= neighbor_cost:
                        continue
                    else:
                        closed.discard(neighbor)
                        f = gScore[neighbor] + euclidian(source=neighbor, dest=dest)
                        open.put((f, neighbor))
                        inOpen.add(neighbor)
                else:
                    f = gScore[neighbor] + euclidian(source=neighbor, dest=dest)
                    open.put((f, neighbor))
                    inOpen.add(neighbor)
                gScore[neighbor] = neighbor_cost
                parents[neighbor] = current
        prev = current
        closed.add(current)
    if current != dest:
        return False
    else:
        return True

    
def add_edge_to_graph(G, e1, e2, w):
    """helper function to efficently add weighted edges and nodes with coordinates as well
    Args:
        G (networkx.classes.graph.Graph): A 2D grid graph
        e1 (int): _description_
        e2 (int): _description_
        w (int): weight of edge
    """
    G.add_edge(e1, e2, weight=w)
    
def print_path(parents):
    if len(parents) <= 0:
        return

def tupleBuilder(a, b):
    a = int(a)
    b = int(b)
    return (a, b)
    