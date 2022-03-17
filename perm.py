def rotate(word, list):
    word.insert(0, word[-1])
    word.pop()
    list.append("".join(word))

def  x():
    word=list('abcd')
    list=[]
    l = len(word)
    for i in range(l):
        word[0], word[i]=word[i],  word[0]
        list.append("".join(word))

    list1=[]
    for  i in list:
        rotate(word, list1)

    print(list1)
    print(list)

#abc
#acb
#bca
#bac
#cba
#cab
perms=[]
def a(l):
    w="".join(l)
    perms.append(w)
    print(w,perms)
    return w;

def  b(w1,w2):
    return w1+w2
def perm0(word):
    l = len(word)
    if  l==1:
        return perms
    mid = int(l/2) if l%2==0 else int((l+1)/2)
    word1=word[0:mid]
    word2=word[mid+1:l]
    b(word1,word2)
    a(word2+word1)
    
def  perm1(w1,w2):
    # print(w1, w2)
    if  len(w1)==0:
        print("--->",w2)
        return
    for i in range(len(w1)):
        c = w1[i:i+1]
        #print(i,c)
        w1p =  w1[0:i]+w1[i+1:len(w1)]
        #print("c,w1",c,w1)
        w2p=w2+c
        perm1(w1p,w2p)

perm1('abcd','')

    
    