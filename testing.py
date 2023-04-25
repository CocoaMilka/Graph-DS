from graph import *

vertices = {1, 2, 3, 4, 5, 6, 7, 8, 9}

test = Graph(vertices)

test.printVertices()

print("Adding vertices...")

# Graph from P1 H4

test.addEdge(1, 2)
test.addEdge(1, 3)

test.addEdge(2, 4)
test.addEdge(2, 5)
test.addEdge(2, 6)

test.addEdge(3, 4)
test.addEdge(3, 5)
test.addEdge(3, 6)

test.addEdge(4, 7)
test.addEdge(4, 8)

test.addEdge(5, 7)
test.addEdge(5, 8)

test.addEdge(6, 7)
test.addEdge(6, 8)

test.addEdge(7, 9)

test.addEdge(8, 9)


test.printAdjacentList()
test.printVisited()

breadthFirstSearch(1, test)
depthFirstSearch(1, test)