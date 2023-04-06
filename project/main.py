import networkx as nx
import math
import random
import matplotlib.pyplot as plt
from functions import *

#what I want to do
"""
Heuristics:
    Euclidian Distance
    Manhattan Distance
    Lp Space Heuristics
    make sure to check office hour video to see other types of heuistics
Classes:
Make graphs"""
G = nx.Graph()

#            0       1         2       3       4        5       6
points = [(1, 7), (8, 10), (12, 8), (5, 4), (2, 1), (12, 2), (5, 16)]  # (x,y) points
edges = [(0, 1, 12), (1, 2, 7), (2, 3, 24), (0, 3, 6), (3, 4, 9), (2, 5, 17), (6, 1, 42), (3, 5, 8), (6, 0, 35), (0, 4, 5)]  # (u, v, weight) edges

for i in range(len(points)):
    G.add_node(points[i], coords=points[i])

for i in range(len(edges)):
    add_edge_to_graph(G, points[edges[i][0]], points[edges[i][1]], edges[i][2])
# Custom graph layout
pos = {point: point for point in points}


# Debug Stuff
# for i in range(0, len(G.nodes)):
#     print(list(G.nodes)[i])
# print(type(G.nodes[(1,7)]))
# print(G.nodes[(1,7)]['coords'])
# print(G.nodes[0])
print(G.edges)
print(G.get_edge_data((1, 7), (2, 1)).get('weight'))
print(type(G.get_edge_data((1, 7), (2, 1)).get('weight')))



# for k in G.nodes():
#     print(k," ",type(k))

# ABOVE LINE IS HOW TO ACCESS NODES
# adding axis
fig, axis = plt.subplots()
edge_labels = nx.get_edge_attributes(G, 'weight')



nx.draw(G, pos=pos, ax=axis)
nx.draw_networkx_nodes(G, pos, node_size=400, ax=axis)
nx.draw_networkx_edges(G, pos, ax=axis)
nx.draw_networkx_labels(G, pos, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels)
plt.axis('on')
axis.set_xlim(0, 20)
axis.set_ylim(0, 20)
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
a = a_star_2(G, source, dest)
print(a)
# f = nx.Graph()
# f = nx.grid_2d_graph(1,2)


# f.add_edge(2,3)
# nx.draw(f, with_labels=True)
# plt.savefig("f.png")
