"# amazon-review-network-analysis" 

This project analyzes Amazon product reviews using Social Network Analysis techniques.

## Dataset
The dataset used in this project is available on Kaggle:

https://www.kaggle.com/datasets/jillanisofttech/amazon-product-reviews

Due to its large size, the dataset is not included in this repository.

## Project Description

The dataset contains product reviews where:

- Users write reviews for products
- Each review represents a relationship between a user and a product

This relationship is modeled as a graph where:

- Nodes represent users and products
- Edges represent reviews

The project applies several graph algorithms to analyze the network.

## Algorithms Implemented

1. Eigenvector Centrality  
Used to identify the most influential nodes in the network.

2. Shortest Path  
Used to compute the shortest connection between two nodes.

3. Clustering Coefficient  
Used to measure the tendency of nodes to form clusters.

4. centerality-degree
5. centrality_betweenness
6. centrality_closeness
7. eccentricity
8. degree_distribution

## Technologies Used

- Python
- NetworkX
- Pandas
- Matplotlib
- Numpy

## Project Structure

graph_builder.py → builds the graph from dataset
eigenvector_centrality.py → computes centrality values
shortest_path.py → finds shortest path between nodes
clustering_coefficient.py → calculates clustering coefficient
and so on......


## How to Run

Install dependencies:

pip install -r requirements.txt


Run scripts:


python eigenvector_centrality.py
python shortest_path.py
python clustering_coefficient.py
and so on.....  


## Author

Amnaa Mohammed