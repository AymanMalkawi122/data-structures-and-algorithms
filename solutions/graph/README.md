# Graph

## Task: Implement a Graph Class

## Approach & Efficiency

### Approach

* The Graph class is implemented using an adjacency list representation, where each vertex is associated with a dictionary of its neighbors and their
corresponding edge weights.
* The add_vertex method adds a vertex to the graph by creating an entry in the vertices_map dictionary with an empty dictionary as its value.
* The add_edge method adds an edge between two vertices by updating the vertices_map dictionaries of both vertices with the appropriate weight.
* The get_vertices method returns a list of all vertices in the graph by extracting the keys from the vertices_map dictionary.
* The get_neighbors method returns a list of neighbors for a given vertex by extracting the keys from the dictionary associated with that vertex in the vertices_map.
* The size method returns the number of vertices in the graph by calculating the length of the list of vertices obtained from the get_vertices method.

### Efficiency

* **Time complexity**:
* Adding a vertex (add_vertex): O(1)
* Adding an edge (add_edge): O(1)
* Getting vertices (get_vertices): O(V), where V is the number of vertices
* Getting neighbors (get_neighbors): O(E), where E is the number of edges connected to the given vertex
* Getting the size (size): O(V), where V is the number of vertices

* **Space complexity**: The space complexity of the Graph class is O(V + E), where V is the number of vertices and E is the number of edges.

## 3. Solution

The Graph class provides an efficient representation of a graph using an adjacency list. It allows for the addition of vertices and edges and provides methods to retrieve information about the graph's vertices and neighbors. The implementation uses dictionaries to store neighbors and their edge weights, enabling quick access to neighbors and efficient space usage.
