import matplotlib.pyplot as plt
from graph_builder import build_graph

G = build_graph()

degrees = [d for n, d in G.degree()]

plt.figure(figsize=(7,5))
plt.hist(degrees, bins=30, color="skyblue", edgecolor="black")
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()
