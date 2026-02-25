# import networkx as nx
# import pandas as pd

# def create_graph(edges_file):
#     edges = pd.read_csv(edges_file)
#     G = nx.Graph()
#     for _, row in edges.iterrows():
#         G.add_edge(row['From'], row['To'], weight=row['Distance'])
#     return G

# def get_routes(G, origin, destinations):
#     routes = {dest: nx.shortest_path(G, origin, dest, weight='weight') for dest in destinations}
#     return routes


#2 3
import networkx as nx
import pandas as pd

def create_graph(edges_file):
    edges = pd.read_csv(edges_file)
    G = nx.Graph()
    for _, row in edges.iterrows():
        G.add_edge(row['From'], row['To'], weight=row['Distance'])
    return G

def get_routes(G, origin, destinations):
    routes = {dest: nx.shortest_path(G, origin, dest, weight='weight') for dest in destinations}
    return routes








