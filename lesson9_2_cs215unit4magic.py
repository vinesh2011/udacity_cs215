#            animal       speed   weight lifespan brain
#                          (mph)   (kg)  (years) mass (g)
animals = [("dog",          46,   35,     13,  280    ),
           ("elephant",     30, 3500,     50, 6250    ),
           ("frog",          5,    0.5,    8,    3    ),
           ("hippopotamus", 45, 1600,     45,  573    ),
           ("horse",        40,  385,     30, 642     ),
           ("human",        27,   80,     78, 2000    ),
           ("lion",         50,  250,     30,  454    ),
           ("mouse",         8,    0.025,  2,    0.625),
           ("rabbit",       25,    4,     12,   40    ), 
           ("shark",        26,  230,     20,   92    ),
           ("sparrow",      16,    0.024,  7,    2    )]

def importance_rank(items, weights):
    names = [item[0] for item in items]  # get the list of animal names
    scores = [sum([a*b for (a,b) in zip(item[1:], weights)]) for item in items]  # get the list of overall scores for each animal
    print(';scores', scores)
    results = zip(scores,names) # make a list of tuple
    print('results', results)
    res2 = sorted(results) # sort the tuple based on the score
    print(';sorted', sorted)
    return res2

answer = importance_rank(animals, (2,.3,7,.1))

for i in range(len(answer)):
    print (i, answer[i][1], "(", answer[i][0], ")")
items=animals
weights=(2,3,7,1)
names = [item[0] for item in items]
a=[list(zip(item[1:], weights)) for item in items]
print(a)
b=[1,2,3]
c=['a','b','c']
d = zip(b,c)
print(d)
print(list(d))
#scores = list[((a,b) for (a,b) in (item[1:], weights)) for item in items] 
#print(scores)