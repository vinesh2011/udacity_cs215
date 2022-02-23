#
# Write `max`
# 

def max(L):
    max=-1000000
    for l in L:# return the maximum value in L
        if  l>max:
            max=l
    return max

def test():
    L = [1, 2, 3, 4]
    assert 4 == max(L)
    L = [3, 6, 10, 9, 3]
    assert 10 == max(L)


test()