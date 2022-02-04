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

def findPath(edges, visited, eulerian_path, node):
    edges0 = set()
    if verbose:
        print('  ------ findPath  ------   ')
        print("edges0", edges0)
        print("visited0", visited)
        print("eulerian_path0", eulerian_path)
        print("node0", node)
        print('  ------ ------  ------   ')
    for i in edges:
        if i in visited:
            edges0.add(i)
            if verbose:
                print("edges0", edges0)
        elif (node == None) or (node == i[0]) :
            visited.add(i)
            eulerian_path.append(i[0])
            node = i[1]
            if verbose:
                print("visited0", visited)
                print("eulerian_path0", eulerian_path)
        elif node == i[1]:
            visited.add(i)
            eulerian_path.append(i[1])
            node = i[0]
            if verbose:
                print("visited0", visited)
                print("eulerian_path0", eulerian_path)
        else:
            edges0.add(i)
            if verbose:
                print("edges0", edges0)
        if verbose:
            print("node0", node)
            print("---")
    if len(edges0) != 0:
        if len(edges0) == len(edges):
            if verbose:
                print('no solution seems possible from here')
            return []
        else:
            return findPath(edges0, visited, eulerian_path, node)
    return eulerian_path
        #print(1)

def addToDict(dict, x, y):
    if not x in dict:
        dict[x]=[]
    dict[x].append(y)
    
def analyze(graph):
    dict = {}
    connections = {}
    for edge in graph:
        addToDict(dict, edge[0], edge[1])
        addToDict(dict, edge[1], edge[0])
    for key in dict:
        size = len(dict[key])
        if not size in connections:
            connections[size]=[]
        connections[size].append(key)
    #print('dict', dict)
    #print('connections', connections)

def find_eulerian_tour(graph):
    if len(graph) == 0:
        return []
    analyze(graph)
    #exit(3)
    #print("grpah", graph)
    visited = set()
    eulerian_path = []
    try:
        eulerian_path = findPath(graph, visited, eulerian_path, None)
        eulerian_path.append(graph[0][0])
    except BaseException:
        if verbose:
            print('some  error')
        #tb = sys.exc_info()[2]
        #raise OtherException(...).with_traceback(tb)

    #print("visited", visited)
    #print("eulerian_path",  eulerian_path)
    if verbose:
        print(eulerian_path)
    return eulerian_path
