
def get_children(S, root, parent):
    """returns the children from following the
    green edges"""
    return [n for n, e in S[root].items()
            if ((not n == parent) and
                (e == 'green'))]

d  = get_children(
    {'a':{'b':1},
    'b':{'c':1},
    'c':{'d':1},
    'd':{'e':1}
    }, 'a','b')
print(d)