import osmium

class OSMHandler(osmium.SimpleHandler):
    def node(self, n):
        print("Node:", n.id, n.location, dict(n.tags))

    def way(self, w):
        print("Way:", w.id, dict(w.tags), "nodes:", len(w.nodes))

    def relation(self, r):
        print("Relation:", r.id, dict(r.tags))

# Replace the filename with your actual file
handler = OSMHandler()
handler.apply_file("sri-lanka-251122.osm.pbf")
