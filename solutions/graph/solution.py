class Graph:
    def __init__(self):
        self.vertices_map = {}

    def add_vertex(self, value):
        self.vertices_map[value] = {}

    def add_edge(self, vertex1, vertex2, weight = -1):
        if self.vertices_map[vertex1] and self.vertices_map[vertex2]:
            self.vertices_map[vertex1][vertex2] = weight
            self.vertices_map[vertex2][vertex1] = weight
            return
        raise Exception("Invalid vertices")

    def get_vertices(self):
        self.vertices_map.keys()

    def get_neighbors(self, vertex):
        self.vertices_map[vertex].keys()

    def size(self):
        len(self.get_vertices())
