#
# Write centrality_max to return the maximum distance
# from a node to all the other nodes it can reach
#

def centrality_max(G, v):
    if len(G) == 0:
        return 0
    if not v in G:
        return 0
    print('G', G)
    print('------')
    visited = set()
    open_list = [(v,-1)]
    distance={}
    print(len(open_list), open_list[0])
    while len(open_list) !=0:
        currentNode, length0 = open_list[0]
        print('currentNode, length ', currentNode, length0 )
        del open_list[0]
        visited.add(currentNode)
        distance[currentNode] = length0+1
        for node in G[currentNode]:
            if not node in visited:
                length = length0+2
                visited.add(node)
                distance[node] = length
                for n in G[node]:
                    if not n in visited:
                        open_list.append((n, length))
                print('currentNode  node length ==> ' , currentNode, node, (length))
                print('visited_0', visited)
                print('open_list_0', open_list)
                print('distance_0', distance)
                print('------')
    print('length', (length), 'visited', visited)
    print('distance', distance)
    max =0
    for i in distance:
        if distance[i] > max:
            print("max", i, max, distance[i])
            max = distance[i]
    print('------', max)
    return max

#################
# Testing code
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    chain = ((1,2), (2,3), (3,4), (4,5), (5,6))
    G = {}
    for n1, n2 in chain:
        make_link(G, n1, n2)
    assert centrality_max(G, 1) == 5
    assert centrality_max(G, 3) == 3
    tree = ((1, 2), (1, 3),
            (2, 4), (2, 5),
            (3, 6), (3, 7),
            (4, 8), (4, 9),
            (6, 10), (6, 11))
    G = {}
    for n1, n2 in tree:
        make_link(G, n1, n2)
    assert centrality_max(G, 1) == 3
    assert centrality_max(G, 11) == 6

test()