import osmium
import networkx as nx

class OSMParser(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.nodes = {}       # node_id → (lat, lon)
        self.named_nodes = {} # name → node_id
        self.graph = nx.Graph()

    def node(self, n):
        if not n.location.valid():
            return
        
        lat, lon = n.location.lat, n.location.lon
        self.nodes[n.id] = (lat, lon)

        name = n.tags.get("name")
        if name:
            self.named_nodes[name] = n.id

    def way(self, w):
        if len(w.nodes) < 2:
            return
        
        # Add edges for routing
        for i in range(len(w.nodes) - 1):
            n1 = w.nodes[i].ref
            n2 = w.nodes[i+1].ref
            if n1 in self.nodes and n2 in self.nodes:
                self.graph.add_edge(n1, n2)
