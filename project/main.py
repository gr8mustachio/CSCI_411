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
f = nx.grid_2d_graph(9,5)
plt.figure(figsize=(8,8))
coords = {(x,y):(y,-x) for x,y in f.nodes()}
plt.axis('on')
nx.draw(f, pos=coords, node_color='lightblue', with_labels=True)

# edges = {('(0,0)', '(0,1)') : '2nd Street'}
# nx.draw_networkx_edge_labels(f, coords, edge_labels=edges)

plt.savefig("g.png")
plt.close()
# g.add_node(2)
# g.add_node(5)
# g.add_edge(2, 5)
# g.add_edge(1,'G')
# g.add_edge(2,3)
# g.add_edge(3,4)
# g.add_edge(1,4)
# g.add_edge(1,5)
# g.add_edge(4,1)


plt.clf()

# f = nx.Graph()
# f = nx.grid_2d_graph(1,2)


# f.add_edge(2,3)
# nx.draw(f, with_labels=True)
# plt.savefig("f.png")
