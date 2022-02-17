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
def parse_to_tree(G, node):
    visited = set(node)
    redEdges=[]
    open_list=[node]
    while len(open_list) !=0:
        treeNode = open_list.pop(0)
        for otherNodeData in G[treeNode.data]:
            if otherNodeData in visited:
                continue
            if G[treeNode.data][otherNodeData] == "green":
                visited.add(otherNodeData)
                otherTreeNode = Tree(otherNodeData)
                otherTreeNode.parent = treeNode
                treeNode.children.append(otherTreeNode)
            elif G[treeNode.data][otherNodeData] == "red":
                redEdges.append((treeNode.data, otherNodeData))
                redEdges.append((otherNodeData, treeNode.data))
        for otherTreeNode in treeNode.children:
            open_list.append(otherTreeNode)
    return redEdges

def parse_to_tree0(G, visitedNodes, treeNode):
    for otherNode in G[treeNode.data]:
        if otherNode in visitedNodes:
            continue
        if G[treeNode.data][otherNode] == "green":
            visitedNodes.add(otherNode)
            otherTreeNode = Tree(otherNode)
            otherTreeNode.parent = treeNode
            treeNode.children.append(otherTreeNode)
    for otherTreeNode in treeNode.children:
        parse_to_tree0(G, visitedNodes, otherTreeNode)
def mapNode(node, mapping, postOrderCounter):
    if not node.data in mapping:
        postOrderCounter +=1
        mapping[node.data] = postOrderCounter
    return postOrderCounter

def addToList(node, list):
    if not node in list:
        list.append(node)

def post_order_rank(n0):
    mapping = {}
    postOrderCounter=0
    open_list = [n0]
    while len(open_list) !=0:
        #print(mapping, open_list)
        currentNode = open_list.pop(0)
        if currentNode is None:
            continue
        if currentNode in mapping:
            addToList(currentNode.parent, open_list)
        elif all_children_ranked(currentNode, mapping):
            postOrderCounter = mapNode(currentNode, mapping, postOrderCounter)
            addToList(currentNode.parent, open_list)
        elif len(currentNode.children) == 0:
            postOrderCounter = mapNode(currentNode, mapping, postOrderCounter)
            if currentNode.parent is None:
                return mapping
            if all_children_ranked(currentNode.parent, mapping):
                postOrderCounter = mapNode(currentNode.parent, mapping, postOrderCounter)
                addToList(currentNode.parent, open_list)
        else:
            addToList(currentNode, open_list)
            for node in currentNode.children:
                if not node.data in mapping:
                    addToList(node, open_list)
    return mapping
        

def all_children_ranked(parent, mapping):
    for node in parent.children:
        if not node.data in mapping:
            return False
    return True

def post_order(S, root):
    print(S)
    rootNode = Tree(root)
    parse_to_tree(S, rootNode)
    print(str(rootNode))
    mapping = post_order_rank(rootNode)
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
#test_post_order()

##############
def inc(node, mapping):
    if not node.data in mapping:
        mapping[node.data]=0
    mapping[node.data] = mapping[node.data]+1

def incAncestors(node, mapping):
    while node is not None:
        inc(node, mapping)
        node = node.parent            

def number_of_descendants_parse_tree(root):
    mapping={}
    open_list=[root]
    while len(open_list) !=0 :
        node = open_list.pop(0)
        incAncestors(node, mapping)
        for cNode in node.children:
            addToList(cNode, open_list)
    return mapping

def number_of_descendants(S, root):
    print(S)
    rootNode = Tree(root)
    parse_to_tree(S, rootNode)
    print(str(rootNode))
    mapping = number_of_descendants_parse_tree(rootNode)
    print(mapping)
    return mapping

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
test_number_of_descendants()
###############

def lowesr_post_order_rank(root, redEdges):
    mapping={}
    open_list=[root]
    while len(open_list) !=0 :
        
    
    
def lowest_post_order(S, root, po):
    print(S)
    rootNode = Tree(root)
    redEdges = parse_to_tree(S, rootNode)
    print(str(rootNode))
    mapping = lowesr_post_order_rank(rootNode, redEdges)
    # return mapping between nodes of S and the post-order value
    # of that node
    print('mapping_', mapping)
    return mapping
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
