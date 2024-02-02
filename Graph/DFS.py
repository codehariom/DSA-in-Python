import numpy as np

class Graph:

    def __init__(self, vertices):
        self._adjMat = np.zeros((vertices, vertices))
        self._vertices = vertices
        self._visited = [0] * vertices

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
                    count += 1
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
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for j in range(self._vertices):
            if not self._adjMat[j][v] == 0:
                count += 1
        return count

    def display_adjMat(self):
        print(self._adjMat)

    def DFS(self,s):
        if self._visited[s]==0:
            print(s,end=' ')
            self._visited[s]=1
            for j in range(self._vertices):
                if self._adjMat[s][j]==1 and self._visited[j]==0:
                    self.DFS(j)


G = Graph(7)
G.insert_edge(0, 1)
G.insert_edge(0, 5)
G.insert_edge(0, 6)
G.insert_edge(1, 0)
G.insert_edge(1, 2)
G.insert_edge(1, 5)
G.insert_edge(1, 6)
G.insert_edge(2, 3)
G.insert_edge(2, 4)
G.insert_edge(2, 6)
G.insert_edge(3, 4)
G.insert_edge(4, 2)
G.insert_edge(4, 5)
G.insert_edge(5, 2)
G.insert_edge(5, 3)
G.insert_edge(6, 3)
print('Edges:')
G.edges()
print('DFS:')
G.DFS(0)
