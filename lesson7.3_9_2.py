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
                if debug: print('skip', treeNode.data, otherNode)
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

def create_rooted_span(G, root):
    return create_rooted_spanning_tree(G, root)

def create_rooted_spanning_tree(G, root):
    rootNode = Tree(root)
    map={root:rootNode}
    G2 = copy0(G)
    parseChild1(G2, set(root), map, rootNode)
    if debug: print("create_rooted_spanning_tree", G2)
    return G2

###########
def copy0(G):
    G1 = {}
    for i in G:
        G1[i]= {}
        for j in G[i]:
            G1[i][j] = G[i][j]
    return G1
    
def parse_to_tree(G, root):
    global G_cache
    if  G_cache is None:
        G_cache=G
    if rootNode.data is not None:
        return rootNode
    global G1
    G1 = copy0(G)
    rootNode.data = root
    open_list = [rootNode]
    dataToNodeDict[root] = rootNode
    while len(open_list) !=0:
        node = open_list.pop(0)
        for otherNodeData in G1[node.data]:
            if otherNodeData in dataToNodeDict:
                continue
            if G[node.data][otherNodeData] == "green":
                otherTreeNode = Tree(otherNodeData)
                otherTreeNode.parent = node
                node.children.append(otherTreeNode)
                dataToNodeDict[otherNodeData] = otherTreeNode
        for n in node.children:
            open_list.append(n)

    open_list = [rootNode]
    while len(open_list) !=0:
        node = open_list.pop(0)        
        for n in node.children:
            open_list.append(n)            
        for otherNodeData in G1[node.data]:
            if G[node.data][otherNodeData] == "red":
                addChildren(redEdges, node, dataToNodeDict[otherNodeData])
                addChildren(redEdges, dataToNodeDict[otherNodeData], node)
    return rootNode

def post_order_rank(n0):
    mapping = {}
    postOrderCounter=0
    open_list = [n0]
    while len(open_list) !=0:
        if debug: print(mapping, open_list)
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


def post_order(S, root):
    if debug: print(S)
    rootNode = parse_to_tree(S, root)
    if debug: print(str(rootNode))
    mapping = post_order_rank(rootNode)
    if debug: print('mapping_', mapping)
    return mapping

##############

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
    if debug: print(S)
    rootNode = parse_to_tree(S, root)
    if debug: print(str(rootNode))
    mapping = number_of_descendants_parse_tree(rootNode)
    if debug: print("number_of_descendants", mapping)
    return mapping

###############
def agg_post_order_rank(root, po_mapping, checkForLow):
    mapping = {}
    open_list_hash = {root:1}
    open_list = [root]
    while len(open_list) != 0:
        node = popFirst(open_list, open_list_hash)
        if debug: print(node, open_list_hash, mapping)
        #time.sleep(1)
        if len(node.children) == 0:
            mapping[node.data] = node.data
            addToList0(node.parent, open_list, open_list_hash)
        allAncestorMarked = True
        for childNode in node.children:
            if childNode.data in mapping:
                if checkForLow:
                    if po_mapping[childNode.data] < po_mapping[node.data]:  #low
                        mapping[node.data] = childNode.data
                else:
                    if po_mapping[childNode.data] > po_mapping[node.data]:  #high
                        mapping[node.data] = childNode.data
            else:
                allAncestorMarked = False
                addToList0(childNode, open_list, open_list_hash)
        if allAncestorMarked:
            addToList0(node.parent, open_list, open_list_hash)
            if not node.data in mapping:
                mapping[node.data] = node.data
        else:
            addToList0(node, open_list, open_list_hash)
    if  debug: print (mapping)
    return mapping
    
def merge_mapping_for_red_edges(mapping, redEdges, po_mapping, checkForLow):
    for n1 in redEdges:
        val1 = po_mapping[n1.data]
        for n2 in redEdges[n1]:
            val2 = po_mapping[n2.data]
            if checkForLow:
                if val1 < val2:
                    mapping[n2.data]= mapping[n1.data]
            else:
                if val1 > val2:
                    mapping[n2.data]= mapping[n1.data]
    if debug: print('merge_mapping_for_red_edges', mapping)

def mapping_with_rank(rootNode, mapping, po_mapping):
    mapping_with_rank0 = {}
    open_list=[rootNode]
    while len(open_list) != 0:
        n = open_list.pop(0)
        for  n1  in  n.children:
            open_list.append(n1)
        if n.data == mapping[n.data]:
            mapping_with_rank0[n.data] = po_mapping[n.data]
        elif mapping[n.data] in mapping_with_rank0:
            mapping_with_rank0[n.data] = mapping_with_rank0[mapping[n.data]]
        else:
            open_list.append(n)
    return mapping_with_rank0

def lowest_post_order(S, root, po_mapping):
    if debug: print('S', S)
    rootNode = parse_to_tree(S, root)
    if debug: print(rootNode, str(rootNode))
    if debug: print('redEdges', redEdges)
    
    checkForLow=True
    mapping = agg_post_order_rank(rootNode, po_mapping, checkForLow)
    merge_mapping_for_red_edges(mapping, redEdges, po_mapping, checkForLow)

    mapping_with_rank0 = mapping_with_rank(rootNode, mapping, po_mapping)
    if debug: print('lowest_post_order', mapping_with_rank0)
    return mapping_with_rank0



def highest_post_order(S, root, po_mapping):
    rootNode = parse_to_tree(S, root)
    if debug: print(rootNode, str(rootNode))
    if debug: print('redEdges', redEdges)
    #po_mapping = post_order_rank(rootNode)
    checkForLow  = False
    mapping = agg_post_order_rank(rootNode, po_mapping, checkForLow)
    merge_mapping_for_red_edges(mapping, redEdges, po_mapping, checkForLow)

    mapping_with_rank0 = mapping_with_rank(rootNode, mapping, po_mapping)
    if debug: print('highest_post_order', mapping_with_rank0)
    return mapping_with_rank0

#################
def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    bridges=[]
    S = create_rooted_spanning_tree(G, 'a')
    post_order_mapping = post_order(G, 'a')
    number_of_descendants_mapping = number_of_descendants(G, 'a')
    lowest_post_order_mapping = lowest_post_order(G, 'a',  post_order_mapping)
    highest_post_order_mapping = highest_post_order(G, 'a',  post_order_mapping)
    for key in G:
        post_order_rank = post_order_mapping[key]
        descendants_rank = number_of_descendants_mapping[key]
        low_po_rank = lowest_post_order_mapping[key]
        high_po_rank = highest_post_order_mapping[key]
        if debug: print(post_order_rank, descendants_rank,low_po_rank, high_po_rank)
        if high_po_rank <= post_order_rank and low_po_rank > (post_order_rank - descendants_rank):
            if debug: print("key", key)
            node = dataToNodeDict[key]
            if node.parent is not None:
                bridges.append((node.parent.data,  node.data))

    # high <= post_order
    # low > post_order -  descendatats
    if debug: print(bridges)
    return bridges


def addToList0(node, list, hash):
    if node is None:
        return
    if node not in hash:
        hash[node]=1
        list.append(node)

def popFirst(list, hash):
    n = list.pop(0)
    del hash[n]
    return n

def inc(node, mapping):
    if not node.data in mapping:
        mapping[node.data]=0
    mapping[node.data] = mapping[node.data]+1

def incAncestors(node, mapping):
    while node is not None:
        inc(node, mapping)
        node = node.parent            

def mapNode(node, mapping, postOrderCounter):
    if not node.data in mapping:
        postOrderCounter +=1
        mapping[node.data] = postOrderCounter
    return postOrderCounter

def addToList(node, list):
    if not node in list:
        list.append(node)

def all_children_ranked(parent, mapping):
    for node in parent.children:
        if not node.data in mapping:
            return False
    return True
################

def addChildren(dict, child1, child2):
    if not child1 in dict:
        dict[child1] = {}
    dict[child1][child2] = 1
    
def is_chain_graph():
    print('is_chain_graph')

#####   DEF_TESTS   #######
def test_create_rooted_spanning_tree(I,  O):
    S = create_rooted_spanning_tree(I, "a")
    assert S == O

def test_post_order(I, O):
    po = post_order(I, 'a')
    assert po == O

def test_lowest_post_order(I, O):
    po = post_order(I, 'a')
    l = lowest_post_order(I, 'a', po)
    assert l == O

def test_highest_post_order(I, O):
    po = post_order(I, 'a')
    h = highest_post_order(I, 'a', po)
    assert h == O


def test_number_of_descendants(I, O):
    nd = number_of_descendants(I, 'a')
    assert nd == O

def test_bridge_edges():
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]


dataToNodeDict = {}
G_cache =  None
redEdges = {}
G1 = {}
rootNode = Tree(None)
debug = True
I1 = {'a': {'c': 1, 'b': 1}, 
        'b': {'a': 1, 'd': 1}, 
        'c': {'a': 1, 'd': 1}, 
        'd': {'c': 1, 'b': 1, 'e': 1}, 
        'e': {'d': 1, 'g': 1, 'f': 1}, 
        'f': {'e': 1, 'g': 1},
        'g': {'e': 1, 'f': 1} 
        }
O1_post_order = {'a':7,
                    'b':1, 
                    'c':6, 
                    'd':5, 
                    'e':4, 
                    'f':2, 
                    'g':3}
O1_desendants = {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}
O1_highest_post_order = {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}

I2 = {'a': {'b': 1, 'c': 1}, 
        'b': {'c': 1, 'd': 1}, 
        'c': {'d': 1, 'e': 1}, 
        'd': {'e': 1, 'f': 1, 'g': 1}, 
        'e': {'f': 1, 'g': 1, 'a': 1}, 
        'f': {'g': 1, 'a': 1},
        'g': {'a': 1, 'b': 1} 
        }
I3 = {'a': {'b': 1}, 
        'b': {'c': 1}, 
        'c': {'d': 1}, 
        'd': {'e': 1}, 
        'e': {'f': 1}, 
        'f': {'g': 1},
        'g': {'a': 1} 
        }
O3_rooted_spanning_tree = {'a': {'b': 'green', 'g': 'red'},
        'b': {'c': 'green', 'a': 'green'},
        'c': {'d': 'green', 'b': 'green'},
        'd': {'e': 'green', 'c': 'green'},
        'e': {'f': 'green', 'd': 'green'},
        'f': {'g': 'green', 'e': 'green'}, 
        'g': {'a': 'red', 'f': 'green'}
    }
O3_post_order = {'g': 1, 
                'f': 2, 
                'e': 3, 
                'd': 4, 
                'c': 5, 
                'b': 6, 
                'a': 7}
O3_lowest_post_order = {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}
O3_descendants = {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1}
O3_lowest_post_order = {'g': 1, 'f': 1, 'e': 1, 'd': 1, 'c': 1, 'b': 1, 'a': 1}

test_create_rooted_spanning_tree(I3, O3_rooted_spanning_tree)

test_post_order(O3_rooted_spanning_tree, O3_post_order)

test_number_of_descendants(O3_rooted_spanning_tree, O3_descendants)
test_lowest_post_order(O3_rooted_spanning_tree, O3_lowest_post_order)

test_highest_post_order(O3_rooted_spanning_tree, O3_lowest_post_order)

#test_bridge_edges()
