# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs 
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
# 
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1}, 
#      'b': {'a': 1, 'd': 1}, 
#      'c': {'a': 1, 'd': 1}, 
#      'd': {'c': 1, 'b': 1, 'e': 1}, 
#      'e': {'d': 1, 'g': 1, 'f': 1}, 
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1} 
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'}, 
#      'b': {'a': 'green', 'd': 'red'}, 
#      'c': {'a': 'green', 'd': 'green'}, 
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'} 
#      }
#       
class Tree:
    def __init__(self, data):
        self.children = []
        self.parent = None
        self.data = data
        self.isGreen = True
        self.level = 0
    def __str__(self):
        return self.data+"["+str(len(self.children))+"]"
    def __repr__(self):
        return str(self)

def parseChild1(G, visitedNodes, map, treeNode):
    for otherNode in G[treeNode.data]:
        if otherNode in visitedNodes:
            otherTreeNode = map[otherNode]
            if otherTreeNode in treeNode.children  or treeNode in otherTreeNode.children:
                print('skip', treeNode.data, otherNode)
            else:
                if G[treeNode.data][otherNode] == 1:
                    G[treeNode.data][otherNode] = "red"
                    G[otherNode][treeNode.data] = "red"
        visitedNodes.add(otherNode)
        if G[treeNode.data][otherNode] == 1:
            otherTreeNode = Tree(otherNode)
            otherTreeNode.level = treeNode.level+1
            map[otherNode] = otherTreeNode
            treeNode.children.append(otherTreeNode)
            G[treeNode.data][otherNode]  = "green"
            G[otherNode][treeNode.data] = "green"
    #for otherTreeNode in treeNode.children:
            parseChild1(G, visitedNodes, map, otherTreeNode)

def create_rooted_spanning_tree(G, root):
    #parseChild(G,[root],[],root)
    rootNode = Tree(root)
    map={root:rootNode}
    parseChild1(G, set(root), map, rootNode)
    print(G)
    return G

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'}, 
                 'b': {'a': 'green', 'd': 'red'}, 
                 'c': {'a': 'green', 'd': 'green'}, 
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }

###########
def post_order_parse_tree(G, visitedNodes, treeNode):
    for otherNode in G[treeNode.data]:
        if otherNode in visitedNodes:
            continue
        if G[treeNode.data][otherNode] == "green":
            visitedNodes.add(otherNode)
            otherTreeNode = Tree(otherNode)
            otherTreeNode.parent = treeNode
            treeNode.children.append(otherTreeNode)
    for otherTreeNode in treeNode.children:
        post_order_parse_tree(G, visitedNodes, otherTreeNode)

def all_descendants_ranked(currentNode, mapping):
    for node in currentNode.parent.children:
        if not node.data in mapping:
            return False
    return True

def post_order_rank_parent(node, mapping, postOrderCounter):
    nodes_to_rank=[node]
    while len(nodes_to_rank) !=0:
        currentNode = nodes_to_rank.pop(0)
        if currentNode.parent is not None:
            if all_descendants_ranked(currentNode, mapping):
                postOrderCounter +=1
                mapping[currentNode.parent.data] = postOrderCounter
                nodes_to_rank.append(currentNode.parent)
            else:
                for node in currentNode.parent.children:
                    if not node in mapping:
                        nodes_to_parse.append(node)

def rank_node(node, mapping, postOrderCounter, nodes_to_rank):
    if not node.data in mapping:
        nodes_to_rank.append(node.parent) 
        postOrderCounter +=1
        mapping[node.data] = postOrderCounter
        print('mapping', mapping, "nodes_to_rank", nodes_to_rank, node)
    return postOrderCounter

def post_order_rank(n0, mapping, postOrderCounter):
    nodes_to_parse = [n0]
    nodes_to_rank = []
    while (len(nodes_to_parse)+len(nodes_to_rank)) !=0:
        #print(mapping, nodes_to_parse, nodes_to_rank)
        if len(nodes_to_parse) != 0:
            print('nodes_to_parse',mapping, "nodes_to_parse",nodes_to_parse, "nodes_to_rank",nodes_to_rank)
            currentNode = nodes_to_parse.pop()
            if len(currentNode.children) == 0:
                postOrderCounter = rank_node(currentNode, mapping, postOrderCounter, nodes_to_rank)
            else:
                for node in currentNode.children:
                    if not node.data in mapping:
                        nodes_to_parse.append(node)
        elif len(nodes_to_rank) !=0:
            print('nodes_to_rank',mapping, "nodes_to_parse",nodes_to_parse, "nodes_to_rank",nodes_to_rank)
            currentNode1  = nodes_to_rank.pop()
            if currentNode1.parent is None:
                continue
            if all_descendants_ranked(currentNode1, mapping):
                postOrderCounter = rank_node(currentNode1, mapping, postOrderCounter, nodes_to_rank)
            else:
                for node in currentNode1.parent.children:
                    if not node.data in mapping:
                        nodes_to_parse.append(node)

def post_order(S, root):
    print(S)
    rootNode = Tree(root)
    post_order_parse_tree(S, set(root), rootNode)
    print(str(rootNode))
    mapping = {}
    post_order_rank(rootNode,  mapping, 0)
    # return mapping between nodes of S and the post-order value
    # of that node
    print('mapping_', mapping)
    return mapping

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}

##############

def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    pass

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

###############

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    pass

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}


################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    pass

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
    
#################

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    pass

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]

#test_create_rooted_spanning_tree()
test_post_order()