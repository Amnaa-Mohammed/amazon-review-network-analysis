<<<<<<< HEAD
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

print("Loading sample data...")


df = pd.read_csv("clean_reviews.csv", nrows=30)


G = nx.Graph()

for _, row in df.iterrows():
    G.add_node(row["UserId"], type="user")
    G.add_node(row["ProductId"], type="product")
    G.add_edge(row["UserId"], row["ProductId"])

print("Graph built")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

#  Closeness Centrality
print("\nComputing Closeness Centrality...")
cc = nx.closeness_centrality(G)

print("\n--- Top 5 Closeness Centrality ---")
for n in sorted(cc, key=cc.get, reverse=True)[:5]:
    print(f"{n} → {cc[n]:.6f}")




pos = nx.spring_layout(G)

node_sizes = [400 + 2500 * cc[n] for n in G.nodes()]
node_colors = [cc[n] for n in G.nodes()]

fig, ax = plt.subplots(figsize=(9, 9))

nx.draw(
    G,
    pos,
    ax=ax,
    with_labels=False,
    node_size=node_sizes,
    node_color=node_colors,
    cmap=plt.cm.inferno,  
    edge_color="lightgray",
    alpha=0.9
)

ax.set_title("Closeness Centrality (Kamada–Kawai Layout)", fontsize=14)

# Colorbar
norm = Normalize(vmin=min(node_colors), vmax=max(node_colors))
sm = ScalarMappable(norm=norm, cmap=plt.cm.inferno)
sm.set_array([])
fig.colorbar(sm, ax=ax, label="Closeness Centrality")

plt.show()
=======
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

print("Loading sample data...")


df = pd.read_csv("clean_reviews.csv", nrows=30)


G = nx.Graph()

for _, row in df.iterrows():
    G.add_node(row["UserId"], type="user")
    G.add_node(row["ProductId"], type="product")
    G.add_edge(row["UserId"], row["ProductId"])

print("Graph built")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

#  Closeness Centrality
print("\nComputing Closeness Centrality...")
cc = nx.closeness_centrality(G)

print("\n--- Top 5 Closeness Centrality ---")
for n in sorted(cc, key=cc.get, reverse=True)[:5]:
    print(f"{n} → {cc[n]:.6f}")




pos = nx.spring_layout(G)

node_sizes = [400 + 2500 * cc[n] for n in G.nodes()]
node_colors = [cc[n] for n in G.nodes()]

fig, ax = plt.subplots(figsize=(9, 9))

nx.draw(
    G,
    pos,
    ax=ax,
    with_labels=False,
    node_size=node_sizes,
    node_color=node_colors,
    cmap=plt.cm.inferno,  
    edge_color="lightgray",
    alpha=0.9
)

ax.set_title("Closeness Centrality (Kamada–Kawai Layout)", fontsize=14)

# Colorbar
norm = Normalize(vmin=min(node_colors), vmax=max(node_colors))
sm = ScalarMappable(norm=norm, cmap=plt.cm.inferno)
sm.set_array([])
fig.colorbar(sm, ax=ax, label="Closeness Centrality")

plt.show()
>>>>>>> a0441f862306ed2b8fde76c94a903acf56befa41
