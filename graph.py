
class Graph:

    # Member Variables
    vertices = []
    adjacentList = {}
    adjacentCount = {}
    parent = {}
    visited = {}
    level = {}

    # Takes an array of vertices as input
    def __init__(self, vertexList):
        for i in vertexList:
            self.vertices.append(i)
            self.adjacentList[i] = []
            self.adjacentCount[i] = 0
            self.visited[i] = -1
            self.level[i] = 0
    
    # x is the starting vertex and y is the ending vertex
    def addEdge(self, x, y):
        self.adjacentList[x].append(y)
        self.adjacentList[y].append(x)


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

    def printLevel(self):
        print("Level List: ")
        print(self.level)


# External Graph Operations

def breadthFirstSearch(s, G):
    frontier = []
    G.visited[s] = 0
    frontier.append(s)

    while frontier != []:
        u = frontier.pop(0)
        for v in G.adjacentList[u]:
            if G.visited[v] == -1:
                G.visited[v] = 0
                G.level[v] = G.level[u] + 1
                G.parent[v] = u
                frontier.append(v)
        G.visited[u] = 1
    
    print(G.level)

def depthFirstSearch(s, G):
    frontier = []
    G.visited[s] = 0
    frontier.append(s)

    while frontier != []:
        u = frontier[len(frontier) - 1]
        for v in G.adjacentList[u]:
            if G.visited[v] == -1:
                G.visited[v] = 0
                G.parent[v] = u
                frontier.append(v)
                break
            else:
                G.adjacentCount[u] += 1
        if G.adjacentCount[u] == len(G.adjacentList[u]):
            G.visited[u] = 1
            frontier.pop()