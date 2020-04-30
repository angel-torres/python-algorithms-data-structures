from queue import Queue
from stack import Stack

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

    def bft(self, vertex):
        visited = set()
        path = []
        plan_to_visit = Queue()

        plan_to_visit.queue(vertex)

        while plan_to_visit.size > 0:
            current_vertex = plan_to_visit.dequeue()
            if current_vertex not in visited:
                visited.add(current_vertex)
                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    if neighbor not in visited:
                        plan_to_visit.queue(neighbor)
        
        return path
    
    def dft(self, vertex):
        plan_to_visit = Stack()
        visited = set()

        plan_to_visit.push(vertex)

        while plan_to_visit.size > 0:
            current_vertex = plan_to_visit.pop()

            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)

                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    plan_to_visit.push(neighbor)
        
    def bfs(self, v1, v2):
        plan_to_visit = Queue() 
        visited = set()

        plan_to_visit.queue([v1]) 

        while plan_to_visit.size > 0:
            current_path = plan_to_visit.dequeue()
            current_vertex = current_path[-1]

            if current_vertex == v2:
                print(current_path)
                return current_path

            if current_vertex not in visited:
                visited.add(current_vertex)
                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    new_list = list(current_path)
                    new_list.append(neighbor)
                    plan_to_visit.queue(new_list)

    def dfs(self, v1, v2):
        plan_to_visit = Stack()
        visited = set()

        plan_to_visit.push([v1])

        while plan_to_visit.size > 0:
            current_path = plan_to_visit.pop()
            current_vertex = current_path[-1]

            if current_vertex == v2:
                print(current_path)
                return current_path
            
            if current_vertex not in visited:
                visited.add(current_vertex)

                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    plan_to_visit.push(new_path)




if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # graph.bfs(1, 6)

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    graph.dfs(1, 6)
    # print(graph.dfs_recursive(1, 6))