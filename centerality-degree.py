import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

print("Loading small sample from CSV...")

# --------- SAMPLE FROM CSV FIRST ---------
df = pd.read_csv("clean_reviews.csv", nrows=300)

G = nx.Graph()

for _, row in df.iterrows():
    G.add_node(row["UserId"], type="user")
    G.add_node(row["ProductId"], type="product")
    G.add_edge(row["UserId"], row["ProductId"])

print("Graph built:")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# --------- Degree Centrality ---------
deg = nx.degree_centrality(G)

pos = nx.spring_layout(G, seed=42)

node_sizes = [2000 * deg[n] + 300 for n in G.nodes()]
node_colors = [deg[n] for n in G.nodes()]

fig, ax = plt.subplots(figsize=(8,8))

nx.draw(
    G,
    pos,
    ax=ax,
    with_labels=False,
    node_size=node_sizes,
    node_color=node_colors,
    cmap=plt.cm.plasma,
    edge_color="gray"
)

ax.set_title("Degree Centrality")

norm = Normalize(vmin=min(node_colors), vmax=max(node_colors))
sm = ScalarMappable(norm=norm, cmap=plt.cm.plasma)
sm.set_array([])
fig.colorbar(sm, ax=ax, label="Degree Centrality")

plt.show()
