#
# Implement remove_min
#
import printTree

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

# Call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its immediate children
def down_heapify(L, i):
    # If i is a leaf, heap property holds
    if is_leaf(L, i): 
        return
    # If i has one child...
    if one_child(L, i):
        # check heap property
        if L[i] > L[left_child(i)]:
            # If it fails, swap, fixing i and its child (a leaf)
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        return
    # If i has two children...
    # check heap property
    if min(L[left_child(i)], L[right_child(i)]) >= L[i]: 
        return
    # If it fails, see which child is the smaller
    # and swap i's value into that child
    # Afterwards, recurse into that child, which might violate
    if L[left_child(i)] < L[right_child(i)]:
        # Swap into left child
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        down_heapify(L, left_child(i))
        return
    else:
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        down_heapify(L, right_child(i))
        return

def remove_min(L):
    last_node = L.pop()
    L[0] = last_node
    down_heapify(L, 0)
    return L


def insert_to_heap(L, e):
    L.append(e)
    n = len(L)
    fix_heap_for_insert(L, n-1)

def fix_heap_for_insert(L,i):
    print(i, L)
    if i == 0: return
    pi = int(parent(i))
    if L[i] < L[pi]:
        (L[i], L[pi]) = (L[pi], L[i])
        fix_heap_for_insert(L, pi)

def get_top_k(k, L):
    L =list(reversed(range(10)))
    build_heap(L)
    lk= L[0:k]
    build_heap(lk)

#########
# Testing Code
#

# build_heap
def build_heap(L):
    #for i in range(len(L)):
    for i in range(len(L)-1, -1, -1):
        down_heapify(L, i)
        print(i,L)

def test_print_tree3(L, i=0, level=0):
    print ('    ' * level + str(L[i]))
    level +=1
    l  = left_child(i)
    if l <len(L):
        test_print_tree3(L, l, level)
    r  = right_child(i)
    if r <len(L):
        test_print_tree3(L, r, level)

def test_insert_min():
    L = list(reversed(range(10)))
    print("range", L)
    build_heap(L)
    print("heap", L)
    insert_to_heap(L, -1)
    print("after_remove_min", L)
    # now, the new minimum should be 1
    assert L[0] == 1

def test_remove_min():
    L = list(reversed(range(10)))
    print("range", L)
    down_heapify(L,0)
    print("heap", L)
    L2  = remove_min(L)
    print("after_remove_min", L2)
    # now, the new minimum should be 1
    assert L[0] == 1

def test_insert_to_heap():
    L = list(range(30))
    build_heap(L)
    insert_to_heap(L, -1)
    print(L)    
    printTree.BstNode.print_tree(L)

test_remove_min()

test_insert_to_heap()

