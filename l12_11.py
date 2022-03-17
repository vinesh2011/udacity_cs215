from typing import Dict, Union, Any


def append(obj, k, v):
    if k not in obj:
        obj[k] = []
    obj[k].append(v)


def add(obj, k, v):
    if k not in obj:
        obj[k] = 0
    obj[k] += v


def set_min(obj, k, v):
    if k not in obj:
        obj[k] = v
    elif obj[k] < v:
        obj[k] = v
    else:
        print(3)


def can_continue(n, visited, G):
    if n in visited:
        return True
    else:
        visited[n] = 1
        return n not in G


visited_nodes = {}
min_distance = {}
distance = {}
visited_edges = {}
connections={}


def djikistra(G, src):
    open_list = [src]
    while len(open_list) != 0:
        n = open_list.pop(0)
        if can_continue(n, visited_nodes, G):
            continue
        for k, v in G[n].items():
            distance[(n, k)] = v
            open_list.append(k)
    print('distance', distance)
    print('visited', visited_nodes)

    for dest in visited_nodes:
        if dest == src:
            continue
    find_min_distance(G, src, dest)

def find_minn_distance(G, src, dest):
    open_list = [src]
    while len(open_list) != 0:
        src = open_list.pop(0)
        n = src
        if n in connections:
            connections[n] = []
        path = connections[n]
        for k, v in G[src].items():
            if k == dest:
                set_min(path, (n, dest), v)
            else:
                if (n, k) in distance:
                    append(path, (n, k), v)
                    open_list.append((path,k,dest))
    print('min', min_distance)
    print('distance', distance)
    print('visited', visited_nodes)
    print('open_list', open_list)
    print('------')


K: dict = {'a': {'b': 5, 'c': 3}, 'b': {'c': 1, 'd': 4}}#, 'c': {'e': 3, 'f': 1}, 'd': {'f': 5}}
djikistra(K, 'a')
