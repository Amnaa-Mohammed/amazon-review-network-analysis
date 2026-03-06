<<<<<<< HEAD

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


df = pd.read_csv("clean_reviews.csv")

# undirekted DRAW network
G = nx.Graph()

for i, row in df.iterrows():
    user = row["UserId"]
    prod = row["ProductId"]
    G.add_node(user, type="user")
    G.add_node(prod, type="product")
    G.add_edge(user, prod)

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

sample_nodes = list(G.nodes())[:30]   
SG = G.subgraph(sample_nodes)

user_nodes = [n for n, d in SG.nodes(data=True) if d["type"] == "user"]
product_nodes = [n for n, d in SG.nodes(data=True) if d["type"] == "product"]

plt.figure(figsize=(8,6))
pos = nx.spring_layout(SG, k=1.5)

nx.draw_networkx_nodes(SG, pos, nodelist=user_nodes, node_color="skyblue", node_size=400, label="Users")
nx.draw_networkx_nodes(SG, pos, nodelist=product_nodes, node_color="lightgreen", node_size=400, label="Products")
nx.draw_networkx_edges(SG, pos, edge_color="black", width=1.5)
nx.draw_networkx_labels(SG, pos, font_size=7)

plt.legend()
plt.title("Sample User–Product Network")
plt.show()


# Weighted Graph
WG = nx.Graph()

for i, row in df.iterrows():
    u = row["UserId"]
    p = row["ProductId"]
    
    if WG.has_edge(u, p):
        WG[u][p]["weight"] += 1
    else:
        WG.add_edge(u, p, weight=1)
print("Weighted Graph:")
print("Nodes:", WG.number_of_nodes())
print("Edges:", WG.number_of_edges())
sample_Wnodes = list(WG.nodes())[:30]  
SWG = WG.subgraph(sample_Wnodes)
pos = nx.circular_layout(SWG)  


nx.draw_networkx_nodes(SWG, pos, node_size=700, node_color='skyblue')


edges = SWG.edges(data=True)
nx.draw_networkx_edges(SWG, pos, edgelist=edges, width=[d['weight'] for (u,v,d) in edges])


nx.draw_networkx_labels(SWG, pos, font_size=10, font_color='black')


edge_labels = nx.get_edge_attributes(SWG, 'weight')
nx.draw_networkx_edge_labels(SWG, pos, edge_labels=edge_labels)


plt.axis('off')
plt.show()




=======

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


df = pd.read_csv("clean_reviews.csv")

# undirekted DRAW network
G = nx.Graph()

for i, row in df.iterrows():
    user = row["UserId"]
    prod = row["ProductId"]
    G.add_node(user, type="user")
    G.add_node(prod, type="product")
    G.add_edge(user, prod)

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

sample_nodes = list(G.nodes())[:30]   
SG = G.subgraph(sample_nodes)

user_nodes = [n for n, d in SG.nodes(data=True) if d["type"] == "user"]
product_nodes = [n for n, d in SG.nodes(data=True) if d["type"] == "product"]

plt.figure(figsize=(8,6))
pos = nx.spring_layout(SG, k=1.5)

nx.draw_networkx_nodes(SG, pos, nodelist=user_nodes, node_color="skyblue", node_size=400, label="Users")
nx.draw_networkx_nodes(SG, pos, nodelist=product_nodes, node_color="lightgreen", node_size=400, label="Products")
nx.draw_networkx_edges(SG, pos, edge_color="black", width=1.5)
nx.draw_networkx_labels(SG, pos, font_size=7)

plt.legend()
plt.title("Sample User–Product Network")
plt.show()


# Weighted Graph
WG = nx.Graph()

for i, row in df.iterrows():
    u = row["UserId"]
    p = row["ProductId"]
    
    if WG.has_edge(u, p):
        WG[u][p]["weight"] += 1
    else:
        WG.add_edge(u, p, weight=1)
print("Weighted Graph:")
print("Nodes:", WG.number_of_nodes())
print("Edges:", WG.number_of_edges())
sample_Wnodes = list(WG.nodes())[:30]  
SWG = WG.subgraph(sample_Wnodes)
pos = nx.circular_layout(SWG)  


nx.draw_networkx_nodes(SWG, pos, node_size=700, node_color='skyblue')


edges = SWG.edges(data=True)
nx.draw_networkx_edges(SWG, pos, edgelist=edges, width=[d['weight'] for (u,v,d) in edges])


nx.draw_networkx_labels(SWG, pos, font_size=10, font_color='black')


edge_labels = nx.get_edge_attributes(SWG, 'weight')
nx.draw_networkx_edge_labels(SWG, pos, edge_labels=edge_labels)


plt.axis('off')
plt.show()




>>>>>>> a0441f862306ed2b8fde76c94a903acf56befa41
