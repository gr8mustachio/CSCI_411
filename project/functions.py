import networkx as nx
import math
def euclidian(source, dest):
    """The Euclidian Distance Formula is used to find the distance between two points
    This function takes in two coords with format [x,y] and returns the Euclidian distance between the two points

    Returns:
        _type_: float
    """
    distance = math.sqrt((dest[0] - source[0])**2 + (dest[1] - source[1])**2)
    return distance

def manhattan(source, dest):
    """Manhattan Distabce Fr=ormula is isued to calculate the manhattan distance from two point

    Args:
        source (list): [x1, y1]
        dest (list): [x2, y2]]

    Returns:
        _type_: int
    """
    distance = abs(source[0] - dest[0]) + abs(source[1] - dest[1])
    return distance

def a_star(G, source, dest):
    return None