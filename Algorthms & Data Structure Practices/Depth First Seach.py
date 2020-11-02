#Scott Hawley

"""
Graph with DepthFirstSearch
"""
from collections import defaultdict

class Graph:
    #create a dictionary to store graph
    def __init__(self):
        self.graph = defaultdict(list)

    #add an edge to the graph
    def addEdge(self,u,vertex):
        self.graph[u].append(vertex)

    def DepthFirstRecurtion(self, source, visited):
        #this function will print the current source, and then recursively
        #call a new source to print, visited nodes will not reappear
        visited[source] = True
        print(source, end = " ")
        
        for x in self.graph[source]:
            if visited[x] == False:
                self.DepthFirstRecurtion(x, visited)
    
    def DepthFirstSearch(self, source):
        #keep track of visted nodes, all start false
        visited = [False] * (len(self.graph))
        #call a recursive function
        self.DepthFirstRecurtion(source, visited)

        

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

print("Depth First Traversal from 3: ")
graph.DepthFirstSearch(3)

