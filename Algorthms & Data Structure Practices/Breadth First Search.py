#Scott Hawley

"""
Graph with Breadth First Search
"""
from collections import defaultdict

class Graph:
    #create a dictionary to store graph
    def __init__(self):
        self.graph = defaultdict(list)

    #add an edge to the graph
    def addEdge(self,u,vertex):
        self.graph[u].append(vertex)

    def BreadthFirstSearch(self, source):
        #keep track of visted nodes, all start false
        visited = [False] * (len(self.graph))

        #create a queue and add the source node to it
        #the source node is visited
        queue = []
        queue.append(source)
        visited[source] = True
        while queue:
            #visit each vertex and pop it from queue
            source = queue.pop(0)
            print(source, end = " ")
            for x in self.graph[source]:
                if visited[x] == False:
                    queue.append(x)
                    visited[x] = True

"""
Driver Code
"""
graph = Graph()
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(1, 4)
graph.addEdge(2, 3)
graph.addEdge(3, 1)
graph.addEdge(4, 0)

print("Breadth First Traversal from 3: ")
graph.BreadthFirstSearch(3)

