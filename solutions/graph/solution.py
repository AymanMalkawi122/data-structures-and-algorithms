class Graph:
    def __init__(self):
        self.vertices_map = {}

    def add_vertex(self, value):
        """
        Add a vertex with the given 'value' to the graph.
        """
        self.vertices_map[value] = {}

    def add_edge(self, vertex1, vertex2, weight=-1):
        """
        Add an edge between 'vertex1' and 'vertex2' with the given 'weight'.
        """
        if self.vertices_map[vertex1] != None and self.vertices_map[vertex2] != None:
            self.vertices_map[vertex1][vertex2] = weight
            self.vertices_map[vertex2][vertex1] = weight
        else:
            raise Exception("Invalid vertices")

    def get_vertices(self):
        """
        Get a list of all vertices in the graph.
        """
        return list(self.vertices_map.keys())

    def get_neighbors(self, vertex):
        """
        Get a list of neighbor vertices of the given 'vertex'.
        """
        return self.vertices_map[vertex]

    def size(self):
        """
        Get the number of vertices in the graph.
        """
        return len(self.get_vertices())
