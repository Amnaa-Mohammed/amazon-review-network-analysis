import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

print("Loading sample data...")

# -------- SAMPLE FROM CSV --------
df = pd.read_csv("clean_reviews.csv", nrows=300)   

# -------- BUILD GRAPH --------
G = nx.Graph()

for _, row in df.iterrows():
    G.add_node(row["UserId"], node_type="user")
    G.add_node(row["ProductId"], node_type="product")
    G.add_edge(row["UserId"], row["ProductId"])

print("Graph built")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# -------- EIGENVECTOR CENTRALITY --------
print("\nComputing Eigenvector Centrality (sample)...")
ec = nx.eigenvector_centrality(G, max_iter=500)

print("\n--- Top 5 Eigenvector Centrality ---")
for n in sorted(ec, key=ec.get, reverse=True)[:5]:
    print(f"{n} → {ec[n]:.6f}")

# -------- GRAPH VISUALIZATION --------
print("\nDrawing graph...")

plt.figure(figsize=(12, 8))

# layout
pos = nx.spring_layout(G, seed=42)


user_nodes = [n for n, d in G.nodes(data=True) if d["node_type"] == "user"]
product_nodes = [n for n, d in G.nodes(data=True) if d["node_type"] == "product"]

#draw nodes
nx.draw_networkx_nodes(G, pos,
                       nodelist=user_nodes,
                       node_size=50,
                       alpha=0.7,
                       label="Users")

nx.draw_networkx_nodes(G, pos,
                       nodelist=product_nodes,
                       node_size=50,
                       alpha=0.7,
                       label="Products")

#draw graph
nx.draw_networkx_edges(G, pos, alpha=0.3)

plt.title("Amazon Reviews Bipartite Graph (Users ↔ Products)")
plt.legend()
plt.axis("off")
plt.show()
