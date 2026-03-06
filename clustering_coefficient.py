import networkx as nx
from graph_builder import build_graph

# -------- BUILD GRAPH FROM SAMPLE ONLY --------
G = build_graph(limit=30)  

print("\n--- Clustering Coefficient (Sample = 30) ---")


for node in list(G.nodes())[:1]:
    print("Node:", node)
    print("Clustering Coefficient:", nx.clustering(G, node))


print("Average clustering:", nx.average_clustering(G))

