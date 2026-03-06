# graph_builder.py
import pandas as pd
import networkx as nx

def build_graph(limit=30):
    df = pd.read_csv("clean_reviews.csv")

    G = nx.Graph()

    for _, row in df.iterrows():
        G.add_node(row["UserId"], type="user")
        G.add_node(row["ProductId"], type="product")
        G.add_edge(row["UserId"], row["ProductId"])

    return G
