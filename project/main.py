import networkx as nx
import math
import random
import matplotlib.pyplot as plt
from functions import *


"""
My A* algorithm doesn't quite work as expected all the time, sometimes it takes the wrong path path and overestimates the shortest path
I've spent a bunch of time trying to debug it, and lines 65-68 in functions.py help a bit,
but it's still not perfect. I'm sorry I couldn't figure it out in time, I spent too much
time trying to master networkx before I even started implementing the algorithm.
I was also trying to a test on a grid graph after the first graph, but since this bug 
reared it's head I've spent all my time trying to solve it.

TEST CASES
enter any pair of valid nodes (x1, y1) (x2, y2) and observe the outputted list to see if it is identical
to the netowkx a* traversal algorithm
"""
G = nx.Graph()

#            0       1         2       3       4        5       6         7        8         9
points = [(1, 7), (8, 10), (12, 8), (5, 4), (2, 1), (12, 2), (5, 16), (13, 14), (9, 18), (17, 17)]  # (x,y) points
edges = [(0, 1, 12), (1, 2, 7), (2, 3, 24), (0, 3, 6), (3, 4, 9), (2, 5, 17), (6, 1, 42), (3, 5, 8), (6, 0, 35), (0, 4, 5), (1, 7, 17), (1, 3, 18), (6, 8, 11), (7, 8, 23)]  # (u, v, weight) edges

for i in range(len(points)): # initializing nodes
    G.add_node(points[i], coords=points[i])

for i in range(len(edges)): # initializing edges
    add_edge_to_graph(G, points[edges[i][0]], points[edges[i][1]], edges[i][2])

pos = {point: point for point in points} # Custom graph layout





# for k in G.nodes():
#     print(k," ",type(k))

# ABOVE LINE IS HOW TO ACCESS NODES
# adding axis
fig, axis = plt.subplots()
edge_labels = nx.get_edge_attributes(G, 'weight')


# drawing graph
nx.draw(G, pos=pos, ax=axis)
nx.draw_networkx_nodes(G, pos, node_size=400, ax=axis) # drawing nodes
nx.draw_networkx_edges(G, pos, ax=axis) # drawing edges
nx.draw_networkx_labels(G, pos, font_size=10) # drawing node labels (x,y)
nx.draw_networkx_edge_labels(G, pos, edge_labels) # drawing edge labels (weight)
plt.axis('on')
# Setting x/y limits
axis.set_xlim(0, 20)
axis.set_ylim(0, 20)
# Adding numbers to left side and bottom
axis.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.savefig("G2.png")
plt.close()

x1 = input("Please enter x1 coord: ")
y1 = input('Please enter y1 coord: ')
x2 = input('Please enter x2 coord: ')
y2 = input('Please enter y2 coord: ')
source = tupleBuilder(x1, y1)
dest = tupleBuilder(x2, y2)
# print(source, dest)
# source = 


plt.clf()
a = a_star(G, source, dest)
print(a)
print(nx.astar_path(G, source, dest, heuristic=euclidian, weight='weight'))
# f = nx.Graph()
# f = nx.grid_2d_graph(1,2)


# f.add_edge(2,3)
# nx.draw(f, with_labels=True)
# plt.savefig("f.png")
