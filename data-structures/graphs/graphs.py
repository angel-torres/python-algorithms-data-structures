class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

    def dft(self, vertex):
        print(vertex)

new_graph = Graph()
new_graph.add_vertex(1)
new_graph.add_vertex(2)
new_graph.add_vertex(3)
new_graph.add_vertex(4)
new_graph.add_vertex(5)
new_graph.add_vertex(6)
new_graph.add_vertex(7)
new_graph.add_edge(1, 2)
new_graph.add_edge(2, 1)
new_graph.add_edge(1, 3)
new_graph.add_edge(3, 1)
new_graph.add_edge(1, 4)
new_graph.add_edge(4, 1)
new_graph.add_edge(2, 5)
new_graph.add_edge(5, 2)
new_graph.add_edge(2, 6)
new_graph.add_edge(6, 2)
new_graph.add_edge(2, 7)
new_graph.add_edge(7, 2)

print(new_graph.vertices)
print(new_graph.get_neighbors(1))
print(new_graph.dft(1))
