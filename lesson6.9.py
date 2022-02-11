##################################################################
# Traversal...
# Call this routine on nodes being visited for the first time
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked

def traverse(G, node, target, visited):
    edges = G[node]
    if len(edges) == 0:
        return False
    visited.add(node)
    for nextNode in edges:
        if nextNode == target:
            return True
        if not nextNode in visited:
            if traverse(G, nextNode, target, visited):
                return True
    return False

def check_connection(G, v1, v2):
    # Return True if v1 is connected to v2 in G
    # or False if otherwise
    if not v1 in G:
        return False
    visited = set()
    return traverse(G, v1, v2, visited)
    
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'), 
             ('b', 'f'), ('f', 'e'), ('e', 'h')]
    G = {}
    
    for v1, v2 in edges:
        make_link(G, v1, v2)
    assert check_connection(G, "a", "c") == True
    assert check_connection(G, 'a', 'b') == False
    

test()
