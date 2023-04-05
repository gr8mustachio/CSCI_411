import networkx as nx
import math
import matplotlib.pyplot as plt
from functions import euclidian, manhattan, a_star

f = nx.Graph()
j = f.nodes()
g = nx.grid_2d_graph(9,5)
plt.figure(figsize=(8,8))
coords = {(x,y):(y,-x) for x,y in g.nodes()}
print(list(g.nodes(data=True)))
g.add_edges_from([('(0,0)', '(0,1)', {'weight':"1"})])
plt.axis('on')
nx.draw(g, pos=coords, node_color='lightblue', with_labels=True)
print(type(g.nodes.get(1)))
# edges = {('(0,0)', '(0,1)') : '2nd Street'}
# nx.draw_networkx_edge_labels(f, coords, edge_labels=edges)