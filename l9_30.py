#
# Implement remove_min
#
import printTree

import random

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
    #print(i, L)
    if i == 0: return
    pi = int(parent(i))
    if L[i] < L[pi]:
        (L[i], L[pi]) = (L[pi], L[i])
        fix_heap_for_insert(L, pi)

def build_heap(L):
    #for i in range(len(L)):
    for i in range(len(L)-1, -1, -1):
        down_heapify(L, i)
        #print(i,L)

def get_top_k(L, k):
    print("before")
    printTree.BstNode.print_tree(L)
    #build_heap(L)
    print("after_heapify")
    printTree.BstNode.print_tree(L)
    Lk= L[0:k]
    build_heap(Lk)
    print("===  after   heapify  ===")
    printTree.BstNode.print_tree(Lk)            
    for i in L:
        if i < Lk[0]:
            continue
        elif i > Lk[0]:
            if exists(Lk, i):
                continue
            Lk[0] = i
            down_heapify(Lk, 0)
            print("after", i)
            printTree.BstNode.print_tree(Lk)     
    return Lk       

def exists(L, k, idx=0):
    #print(L, k, idx)
    if len(L) <= idx:
        return False
    if k < L[idx]:
        return False
    elif k  == L[idx]:
        return True
    else:
        left_child_idx = left_child(idx)
        if  exists(L, k, left_child_idx):
            return True
        right_child_idx = right_child(idx)
        if exists(L, k, right_child_idx):
            return True
    return False
#########
# Testing Code
#########

def test_insert_min():
    L = list(reversed(range(10)))
    print("before", L)
    printTree.BstNode.print_tree(L)
    build_heap(L)
    #print("heap", L)
    insert_to_heap(L, -1)
    #print("after_remove_min", L)
    # now, the new minimum should be 1
    print("after")
    printTree.BstNode.print_tree(L)
    assert L[0] == -1

def test_remove_min():
    L = list(reversed(range(10)))
    print("before", L)
    printTree.BstNode.print_tree(L)
    build_heap(L)
    #print("heap", L)
    remove_min(L)
    #print("after_remove_min", L2)
    # now, the new minimum should be 1
    print("after")
    printTree.BstNode.print_tree(L)
    assert L[0] == 1

def test_insert_to_heap():
    L = list(range(30))
    print("before", L)
    printTree.BstNode.print_tree(L)
    build_heap(L)
    insert_to_heap(L, -1)
    #print(L)    
    print("after")
    printTree.BstNode.print_tree(L)

def test_get_top_k():
    L=[]
    for _ in range(20):
        i =random.randint(0, 100)
        if not i in L:
            L.append(i)
    #L=list(reversed(range(10)))
    print(L)
    k=6
    Lk=get_top_k(L, k)
    build_heap(L)
    for _ in range(len(L)-k):
        remove_min(L)
    assert Lk[0]==L[0]
    print("L", L)
    print("Lk", Lk)
    Lk_copy = Lk.copy()
    build_heap(Lk)
    assert Lk_copy == Lk

def test_exists():
    L = list(reversed(range(10)))
    print("before", L)
    printTree.BstNode.print_tree(L)
    build_heap(L)
    assert True == exists(L, 6)

def  test():
    test_exists()
    test_get_top_k()
    test_remove_min()
    test_insert_to_heap()
    test_insert_min()

#test()
