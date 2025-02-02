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
    """Manhattan Distance Formula is isued to calculate the manhattan distance from two points in a grid
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
    closed = set() # set to keep track of visited nodes
    gScore = {} # dictionary to store g(x) values
    hScore = {} # dictonary to store h(x) values
    # iniitalizing source's values and pushing it into queue
    gScore[source] = 0
    hScore[source] = gScore[source] + euclidian(source, dest)
    open.put((0, source)) # can have 0 priority since we are still at the source
    inOpen.add(source) # adding to inOpen to stay consistent
    parents = {} # dictionary fo parents
    path = [] # Path that will be printed if a path is found
    parents[source] = source
    prev = source
    while open.empty() == False:
        # I had a bug where if I tried to traverse up->down instead of down->up in reference to (x, y)
        # it would run forever and lines 84-87 help fix it
        neighborList = list(G.neighbors(prev))
        pass
        if open.queue[0] not in neighborList and prev != source:
            throwaway= open.get()
        current = open.get() # current = node with lowest priority
        current = current[1] # current = (x, y) (removing priority)
        inOpen.discard(current)
        gScore[current] = g(G, source, current) # calculating g(x)
        if current not in path:
            path.append(current)
        if current == dest: # we reached our goal
            print("FOUND")
            print(path)
            return True
        else: # we havent reached our goal
            for neighbor in G.neighbors(current):
                # calculating neighbor cost
                neighbor_cost = gScore[current] + G.get_edge_data(current, neighbor).get('weight')
                gScore[neighbor] = g(G, source, neighbor) # calculating g(neighbor)
                if neighbor in inOpen:
                    if gScore[neighbor] <= neighbor_cost:
                        continue # skip to next neighbor
                elif neighbor in closed:
                    if gScore[neighbor] <= neighbor_cost:
                        continue # skip to next neighbor
                    else: # if neighbor_cost is lower, we need to take another look at the node
                        closed.discard(neighbor)
                        f = gScore[neighbor] + euclidian(source=neighbor, dest=dest) # calculating f(neighbor)
                        open.put((f, neighbor)) # adding back into open
                        inOpen.add(neighbor) # consistency
                else: # if neighbor isnt in open or closed
                    f = gScore[neighbor] + euclidian(source=neighbor, dest=dest) #  calculating f(neighbor)
                    open.put((f, neighbor))
                    inOpen.add(neighbor)
                # Setting g(neighbor) and parents[neighbor]
                gScore[neighbor] = neighbor_cost
                parents[neighbor] = current
        prev = current # helps prevent getting stuck along with lines 84-87 
        closed.add(current) # add node to list of visted nodes
    if current != dest: # We've exhausted all possible paths (open is empty)
        return False
    else:
        return True
