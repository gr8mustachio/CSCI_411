import networkx as nx
import math
import matplotlib.pyplot as plt
from functions import euclidian, manhattan

print('hello')
#what I want to do
"""
Heuristics:
    Euclidian Distance
    Manhattan Distance
    Lp Space Heuristics
    make sure to check office hour video to see other types of heuistics
Classes:
Make graphs"""
g = nx.Graph()
# g.add_node(2)
# g.add_node(5)
# g.add_edge(2, 5)
g.add_edge(1,'G')
# g.add_edge(2,3)
# g.add_edge(3,4)
# g.add_edge(1,4)
# g.add_edge(1,5)
g.add_edge(4,1)

plt.figure(1)
nx.draw(g, with_labels=True)
plt.savefig("g.png")
plt.close()

plt.clf()

# f = nx.Graph()
# f = nx.grid_2d_graph(1,2)


# f.add_edge(2,3)
# nx.draw(f, with_labels=True)
# plt.savefig("f.png")
