import time
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
    for otherTreeNode in treeNode.children:
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
def addChildren(dict, child1, child2):
    if not child1 in dict:
        dict[child1] = {}
    dict[child1][child2] = 1
    
def parse_to_tree(G, root):
    dataToNodeDict = {root.data: root}
    redEdges = {}
    open_list = [root]
    while len(open_list) !=0:
        node = open_list.pop(0)
        for otherNodeData in G[node.data]:
            #if G[treeNode.data][otherNodeData] == "red":
                #addChildren(redEdges, treeNode.data, otherNodeData)
                #addChildren(redEdges, otherNodeData, treeNode.data)
            if otherNodeData in dataToNodeDict:
                continue
            if G[node.data][otherNodeData] == "green":
                otherTreeNode = Tree(otherNodeData)
                otherTreeNode.parent = node
                node.children.append(otherTreeNode)
                dataToNodeDict[otherNodeData] = otherTreeNode
        for n in node.children:
            open_list.append(n)

    open_list = [root]
    while len(open_list) !=0:
        node = open_list.pop(0)        
        for n in node.children:
            open_list.append(n)            
        for otherNodeData in G[node.data]:
            if G[node.data][otherNodeData] == "red":
                addChildren(redEdges, node, dataToNodeDict[otherNodeData])
                addChildren(redEdges, dataToNodeDict[otherNodeData], node)
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
    #print(S)
    rootNode = Tree(root)
    parse_to_tree(S, rootNode)
    #print(str(rootNode))
    mapping = post_order_rank(rootNode)
    # return mapping between nodes of S and the post-order value
    # of that node
    #print('mapping_', mapping)
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
    #print(S)
    rootNode = Tree(root)
    parse_to_tree(S, rootNode)
    #print(str(rootNode))
    mapping = number_of_descendants_parse_tree(rootNode)
    #print(mapping)
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

###############
def processIfMin(node, currentMin, newVar, redEdgesUsed, isRedEdge):
    if newVar < currentMin:
        currentMin = newVar
        if isRedEdge:
            redEdgesUsed[node] = 1
        elif node in redEdgesUsed:
            del redEdgesUsed[node]
    return currentMin

def processIfMax(node, currentMin, newVar, redEdgesUsed, isRedEdge):
    if newVar > currentMin:
        currentMin = newVar
        if isRedEdge:
            redEdgesUsed[node] = 1
        elif node in redEdgesUsed:
            del redEdgesUsed[node]
    return currentMin

def lowesr_post_order_rank(root, redEdges, po_mapping, aggFn):
    mapping = {}
    redEdgesUsed = {}
    tempMapping = {}
    open_list_hash={root:1}
    open_list = [root]
    while len(open_list) != 0:
        allDescendantsMapped = True
        node = open_list.pop(0)
        del open_list_hash[node]
        print(node, open_list_hash, mapping)
        time.sleep(1)
        if not node.data in tempMapping:
            tempMapping[node.data] = po_mapping[node.data]
        aggPo = tempMapping[node.data]
        if node in redEdges and not node.data in redEdgesUsed:
            for n in redEdges[node]:
                if not n in mapping:
                    if len(n.children)==0 and len(node.children) ==0:
                        aggPo = aggFn(node, aggPo, po_mapping[n.data], redEdgesUsed, True)
                        mapping[node.data] = aggPo
                        mapping[n.data] = aggPo
                    else:
                        allDescendantsMapped = False
                else:
                    aggPo = aggFn(node, aggPo, mapping[node.data], redEdgesUsed, True)
        for n in node.children:
            if n.data in mapping:
                aggPo = aggFn(node,  aggPo, mapping[n.data], redEdgesUsed, False)
            else:
                allDescendantsMapped = False
                if not n in open_list_hash:
                    open_list.append(n)
                    open_list_hash[n]=1
        if allDescendantsMapped:
            mapping[node.data] = aggPo
        else:
            if not node in open_list_hash:
                open_list.append(node)
                open_list_hash[node]=1
            tempMapping[node.data] = aggPo
    return mapping
    
    
def lowest_post_order(S, root, po_mapping):
    #print('S', S)
    rootNode = Tree(root)
    redEdges = parse_to_tree(S, rootNode)
    #print(rootNode, str(rootNode))
    #print('redEdges', redEdges)
    #po_mapping = post_order_rank(rootNode)
    mapping = lowesr_post_order_rank(rootNode, redEdges, po_mapping, processIfMin)
    # return mapping between nodes of S and the post-order value
    # of that node
    #print('mapping_', mapping)
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    return mapping

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

def highest_post_order(S, root, po_mapping):
    rootNode = Tree(root)
    redEdges = parse_to_tree(S, rootNode)
    mapping = lowesr_post_order_rank(rootNode, redEdges, po_mapping, processIfMax)
    print('mapping',mapping)
    return mapping

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

#test_lowest_post_order()
#test_number_of_descendants()
#test_create_rooted_spanning_tree()
test_highest_post_order()
