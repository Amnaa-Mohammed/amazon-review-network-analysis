<<<<<<< HEAD
import pandas as pd
import networkx as nx

print("Loading small sample from CSV...")

# --------- LOAD DATA ---------
df = pd.read_csv("clean_reviews.csv", nrows=300)

# --------- BUILD GRAPH ---------
G = nx.Graph()

for _, row in df.iterrows():
    G.add_node(row["UserId"], type="user")
    G.add_node(row["ProductId"], type="product")
    G.add_edge(row["UserId"], row["ProductId"])

print("Graph built:")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# --------- DEGREE CENTRALITY ---------
deg = nx.degree_centrality(G)

# --------- SEPARATE USERS & PRODUCTS ---------
users = [(n, deg[n]) for n, d in G.nodes(data=True) if d["type"] == "user"]
products = [(n, deg[n]) for n, d in G.nodes(data=True) if d["type"] == "product"]

# --------- TOP 5 ---------
top_users = sorted(users, key=lambda x: x[1], reverse=True)[:5]
top_products = sorted(products, key=lambda x: x[1], reverse=True)[:5]

# --------- PRINT RESULTS ---------
print("\nTop 5 Users by Degree Centrality:")
for u, v in top_users:
    print(f"User {u} → {v:.4f}")

print("\nTop 5 Products by Degree Centrality:")
for p, v in top_products:
=======
import pandas as pd
import networkx as nx

print("Loading small sample from CSV...")

# --------- LOAD DATA ---------
df = pd.read_csv("clean_reviews.csv", nrows=300)

# --------- BUILD GRAPH ---------
G = nx.Graph()

for _, row in df.iterrows():
    G.add_node(row["UserId"], type="user")
    G.add_node(row["ProductId"], type="product")
    G.add_edge(row["UserId"], row["ProductId"])

print("Graph built:")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# --------- DEGREE CENTRALITY ---------
deg = nx.degree_centrality(G)

# --------- SEPARATE USERS & PRODUCTS ---------
users = [(n, deg[n]) for n, d in G.nodes(data=True) if d["type"] == "user"]
products = [(n, deg[n]) for n, d in G.nodes(data=True) if d["type"] == "product"]

# --------- TOP 5 ---------
top_users = sorted(users, key=lambda x: x[1], reverse=True)[:5]
top_products = sorted(products, key=lambda x: x[1], reverse=True)[:5]

# --------- PRINT RESULTS ---------
print("\nTop 5 Users by Degree Centrality:")
for u, v in top_users:
    print(f"User {u} → {v:.4f}")

print("\nTop 5 Products by Degree Centrality:")
for p, v in top_products:
>>>>>>> a0441f862306ed2b8fde76c94a903acf56befa41
    print(f"Product {p} → {v:.4f}")