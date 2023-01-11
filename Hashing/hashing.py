#Hashing

nBuckets=3


def create():

    global nBuckets

    hSet=[]

    for i in range(nBuckets):

        hSet.append([])

    return hSet

def hashElemt(e):

    global nBuckets

    return e%nBuckets

def insert (hSet, i):

    global nBuckets

    hSet[hashElemt(i)].append(i)

    return

def remove(hSet, i):

    newBucket=[]

    for j in hSet[hashElemt(i)]:

        if j!= i:

            newBucket.append(j)

    hSet[hashElemt(i)] = newBucket

    return

def member(hSet,i):

    return i in hSet[hashElemt(i)]


def test():

    s = create()

    for i in range(40):

        insert(s,i)

    insert(s,325)
    insert(s,325)
    insert(s,987654321)
    print(s)
    print(member(s,325))
    remove(s,325)
    print(member(s,325))
    print(member(s,987654321))



test()


    











    

            
