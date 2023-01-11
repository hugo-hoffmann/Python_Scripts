import string
import random
from grafo import Grafo , Vertices

def get_palavra_do_texto(path_do_texto):
	with open(path_do_texto, 'r') as f:
		texto = f.read()
		texto = ' '.join(texto.split())
		texto = texto.translate(str.maketrans('', '', string.punctuation))

	palavras = texto.split()

	return palavras
def make_grafo(palavras):
	g= Grafo()
	palavra_anterior = None

	for palavra in palavras:

		palavra_vertice = g.get_vertice(palavra)

		if palavra_anterior:
			palavra_anterior.get_vertice(palavra_vertice)

		palavra_anterior = palavra_vertice

	g.gera_mapa_de_probabilidade()

	return g 

def compose(g, palavras , length ):

	coposicao = []
	palavra = g.get_vertice(random.choice(palavras))

	for _ in range(length):

		coposicao.append(palavra.valor)
		palavra = g.get_proxima_palavra(palavra)

	return coposicao

def main():

	palavras = get_palavra_do_texto('letra.txt')
	g = make_grafo(palavras)
	coposicao = compose(g,palavras,100)

	return ' '.join(coposicao)


if __name__ == '__main__':
	print(main())