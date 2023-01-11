#Encontra a n-esima raiz de um valor dado um epsilon

def dentroepsilon (x,y,ep):

    return abs (x-y)<= ep

def par(m):

    return m%2==0

def findRoot (n,val,epsilon):

    assert type(n)==int and (type(val)== float or type(val)==int) and type(epsilon)== float     

    assert n>0 and epsilon > 0


    if par(n) and val <0:

        return None

    low= - abs(val)
    high = max(abs(val),1.0)
    resp = (high + low)/2.0

    while not dentroepsilon (resp**n ,val ,epsilon):

        print("Tentativa:" + str(resp)+ ", Mínimo:"+ str(low)+ ", Máximo:"+ str(high))

        if resp**n < val:

            low = resp

        else:

            high = resp

        resp = (high + low)/2.0

    return  print(str(resp)+" é a raiz "+ str(n)+"-ésima aproximada de " + str(val))

findRoot (2,5,0.01)
