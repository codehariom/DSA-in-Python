import numpy as np

class Graph:

    def __init__(self, vertices):
        self._adjMat = np.zeros((vertices, vertices))
        self._vertices = vertices

    def insert_edge(self, u, v, x=1):
        self._adjMat[u][v] = x

    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count = count + 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i,end=' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i,'--',j)

    def outdegree(self, v):
        count = 0
        for j in range(self._vertices):
            if not self._adjMat[v][j] == 0:
                count = count + 1
        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if not self._adjMat[i][v] == 0:
                count = count + 1
        return count

    def display_adjMat(self):
        print(self._adjMat)


G = Graph(4)
print('Graph Adjacency Matrix')
G.display_adjMat()
print('Vertices: ', G.vertex_count())
G.insert_edge(0, 1, 26)
G.insert_edge(0, 2, 16)
G.insert_edge(1, 0, 26)
G.insert_edge(1, 2, 12)
G.insert_edge(2, 0, 16)
G.insert_edge(2, 1, 12)
G.insert_edge(2, 3, 8)
G.insert_edge(3, 2, 8)
print('Graph Adjacency Matrix')
G.display_adjMat()
print('Edges Count:', G.edge_count())
print('Vertices:')
G.vertices()
print('Edges:')
G.edges()
print('Edges between 1--3:', G.exist_edge(1,3))
print('Edges between 1--2:', G.exist_edge(1,2))
print('Degree of vertex 2:',G.indegree(2))
print('Graph Adjacency Matrix')
G.display_adjMat()
G.remove_edge(1,2)
print('Graph Adjacency Matrix')
G.display_adjMat()
print('Edges between 1--2:', G.exist_edge(1,2))

