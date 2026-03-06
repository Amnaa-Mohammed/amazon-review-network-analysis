import networkx as nx
from graph_builder import build_graph

G = build_graph()
nodes = list(G.nodes())

print("\n--- Shortest Path ---")

if len(nodes) >= 2 and nx.has_path(G, nodes[0], nodes[1]):
    path = nx.shortest_path(G, nodes[0], nodes[1])
    dist = nx.shortest_path_length(G, nodes[0], nodes[1])
    print("Path:", path)
    print("Distance:", dist)
else:
    print("No path found")
