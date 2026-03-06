import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# ==============================
# 1️⃣ Read dataset
# ==============================
print("Loading data...")
df = pd.read_csv("clean_reviews.csv", nrows=300)

# ==============================
# 2️⃣ Build graph
# ==============================
G = nx.Graph()

for _, row in df.iterrows():
    G.add_edge(row["UserId"], row["ProductId"])

print("Graph built")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# ==============================
# 3️⃣ Largest Connected Component
# ==============================
largest_cc = max(nx.connected_components(G), key=len)
G_cc = G.subgraph(largest_cc)

print("Largest CC nodes:", G_cc.number_of_nodes())

# ==============================
# 4️⃣ Eccentricity
# ==============================
ecc = nx.eccentricity(G_cc)

# ==============================
# 5️⃣ Top 5 Eccentricity
# ==============================
top5 = sorted(ecc.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 nodes by Eccentricity:")
for node, value in top5:
    print(f"{node} : {value}")

# ==============================
# 6️⃣ Visualization
# ==============================
pos = nx.spring_layout(G_cc, seed=42)

node_sizes = [400 + ecc[n]*200 for n in G_cc.nodes()]
node_colors = [ecc[n] for n in G_cc.nodes()]

fig, ax = plt.subplots(figsize=(9, 9))

nx.draw(
    G_cc,
    pos,
    ax=ax,
    with_labels=False,
    node_size=node_sizes,
    node_color=node_colors,
    cmap=plt.cm.viridis,
    edge_color="gray"
)

ax.set_title("Eccentricity Visualization")

# Colorbar
norm = Normalize(vmin=min(node_colors), vmax=max(node_colors))
sm = ScalarMappable(norm=norm, cmap=plt.cm.viridis)
sm.set_array([])
fig.colorbar(sm, ax=ax, label="Eccentricity")

plt.show()
