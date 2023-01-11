def findRoot (n,val,epsilon):

    assert type(n)==int and type(val)== float and type(epsilon)== float

    assert n>0 and epsilon > 0

    

    tentativa=0
    low= - abs(val)
    high = max(abs(val),1.0)
    resp = (high + low)/2.0

    while abs(resp ** n - val) >= epsilon and resp <= val:

        print (str(low) , str(high) ,  str(resp))

        tentativa+=1

        if resp**n < val:

            low=resp

        else:

            high=resp

        resp=(high + low)/2.0

    print ("número de tentativas foi " + str(tentativa))

    print(str(resp)+" é a raiz "+ str(n)+"-ésima aproximada de " + str(val))

    return print(resp)

findRoot (2,0.5,0.01)
