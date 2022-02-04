#!/usr/local/opt/python@3.9/bin/python3.9 
# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

verbose = False

def addToDict(x, y,  connections):
    if not x in connections:
        connections[x]=[]
    connections[x].insert(0, y)
    
def analyze(graph):
    connections = {}
    for edge in graph:
        addToDict(edge[0], edge[1], connections)
        addToDict(edge[1], edge[0], connections)
    #print('connections', connections)
    return connections

def copy(c):
    c1={}
    for i in c:
        c1[i] = c[i].copy()
    return c1

def remove(connections, keyNode, valueNode):
    connections[keyNode].remove(valueNode)
    if len(connections[keyNode]) ==0:
        del connections[keyNode]

def getGraph(graph, startNode, nextNode):
    graph0 = graph.copy()
    edge = (startNode, nextNode)
    if not edge in graph:
        edge = (nextNode, startNode)
    if verbose:
        print('getGraph graph', graph)
        print('getGraph edge', edge)
    graph0.remove(edge)
    return graph0
    
def findPath1(graph, startNode):
    if len(graph) == 0:
        return []
    connections1 = analyze(graph)
    if not startNode in connections1:
        return -1
    eulerianPath = []
    connections = copy(connections1)
    for nextNode in connections1[startNode]:
        remove(connections, startNode, nextNode)
        remove(connections, nextNode, startNode)
        eulerianPath.append(nextNode)
        graph0 = getGraph(graph, startNode, nextNode)
        out = findPath1(graph0, nextNode)
        if verbose:
            print('out', out)
            print('graph0', graph0)
            print('nextNode', nextNode)
            print('eulerianPath', eulerianPath)
        if out == -1:
            addToDict(startNode, nextNode, connections)
            addToDict(nextNode, startNode, connections)
        else:
            eulerianPath.extend(out)
            return eulerianPath

def find_eulerian_tour(graph):
    if len(graph) == 0:
        return []
    if verbose:
        print("graph", graph)
    startNode = graph[0][0]
    eulerianPath = [startNode]
    eulerianPath1 = findPath1(graph, startNode)
    eulerianPath.extend(eulerianPath1)

    #print("visited", visited)
    #print("eulerianPath",  eulerianPath)
    if verbose:
        print(eulerianPath)
    return eulerianPath

graph=[(1,2),(2,3),(3,1)]
out =  find_eulerian_tour(graph)
print(out)

graph = [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
out =  find_eulerian_tour(graph)
print(out)

graph = [(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)]
out =  find_eulerian_tour(graph)
print(out)

graph = [(8, 16), (8, 18), (16, 17), (18, 19),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
out =  find_eulerian_tour(graph)
print(out)