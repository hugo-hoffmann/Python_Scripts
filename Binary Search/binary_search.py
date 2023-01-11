def binary_search(lista , alvo, low=None, high=None):

	if low is None:

		low = 0

	if high is None:

		high = len(lista) -1

	if high < low:

		return -1

	ponto_medio = (low + high)// 2
	
	if lista[ponto_medio] == alvo:
		return ponto_medio

	elif alvo < lista[ponto_medio]:
		return binary_search(lista , alvo, low , ponto_medio-1)

	else:
		return binary_search(lista,alvo,ponto_medio+1 , high)