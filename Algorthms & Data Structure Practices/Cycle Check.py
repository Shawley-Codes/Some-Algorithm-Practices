#Scott Hawley

"""
Graph with Cycle Check
"""
from collections import defaultdict

class Graph:
    #create a dictionary to store graph
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.Vert = vertices

    #add an edge to the graph
    def addEdge(self,u,vertex):
        self.graph[u].append(vertex)

    def CycleRecursion(self, node, visited, stack):
        #this function will recursively call to check the connections of each
        #vertex
        visited[node] = True
        stack[node] = True
        
        for x in self.graph[node]:
            if visited[x] == False:
                if self.CycleRecursion(x, visited, stack) == True:
                    return True
            elif stack[x] == True:
                return True
        stack[node] = False
        return False
    
    def Cycle(self):
        #keep track of visted nodes, all start false
        visited = [False] * self.Vert
        stack = [False] * self.Vert
        #loop through each verticy in the graph
        #and call a recursive function for it
        for node in range(self.Vert):
            if visited[node] == False:
                if self.CycleRecursion(node,visited,stack) == True:
                    return True
        return False
        

        

"""
Driver Code
"""
graph = Graph(4)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(1, 4)
graph.addEdge(2, 3)
graph.addEdge(3, 1)
graph.addEdge(4, 0)

if graph.Cycle() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")

