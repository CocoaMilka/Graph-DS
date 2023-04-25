
class Graph:

    # Member Variables
    vertices = []
    adjacentList = {}
    visited = {}
    level = 0

    # Takes an array of vertices as input
    def __init__(self, vertexList):
        for i in vertexList:
            self.vertices.append(i)
            self.adjacentList[i] = []
            self.visited[i] = -1
    
    # x is the starting vertex and y is the ending vertex
    def addEdge(self, x, y):
        self.adjacentList[x].append(y)
        self.adjacentList[y].append(x)

    def breadthFirstSearch(self):
        for i in 

    #def depthFirstSearch(self):
        # stuff

    # Debug functions
    def printVertices(self):
        print("Vertex List: ")
        print(self.vertices)

    def printAdjacentList(self):
        print("Adjacent List: ")
        print(self.adjacentList)
    
    def printVisited(self):
        print("Visited List: ")
        print(self.visited)