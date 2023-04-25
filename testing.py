from graph import *

vertices = {1, 2, 3, 4, 5}

test = Graph(vertices)

test.printVertices()

print("Adding vertices...")

test.addEdge(1, 2)
test.addEdge(1, 4)
test.addEdge(2, 3)

test.printAdjacentList()
test.printVisited()