#Representação da cadeia de Markov
import random

#Definição do grafo por vertices
class Vertices:
	def __init__(self,valor):  # o valor será a palavra		
		self.valor = valor
		self.vertices = {}
		self.adjacente = {} #nos que tem uma aresta com o vertice
		self.vizinhos = []
		self.peso_vizinhos = []

	def add_vertice(self,valor):

		self.vertices[valor] = Vertices(valor)

	def add_vertice_to(self, vertice, peso=0):
		#Adiciona uma aresta ao vertice de input com o peso
		self.adjacente[vertice]=peso

	def get_mapa_probabilidade(self):
		for (vertice,peso) in self.adjacente.items():
			self.vizinhos.append(vertice)
			self.peso_vizinhos.append(peso)
		
	def incrementa_aresta(self,vertice):	
		#Incrementa o peso de uma aresta
		self.adjacente[vertice]=self.adjacente.get(vertice,0)+1

	def proxima_palavra(self):		
		#escolhe a proxima palavra randomicamente baseado no peso
		return random.choices(self.vizinhos, weights = self.peso_vizinhos)[0]

	def get_vertice(self,valor):
		
		if valor not in self.vertices:

			self.add_vertice(valor)

		return self.vertices[valor] 

class Grafo:

	def __init__(self):
		self.vertices = {}

	def get_vetices_valores(self):
		#Diz os de todos os vertices, retorna todas as possiveis palavras
		return set(self.vertices.keys())

	def add_vertice(self,valor):

		self.vertices[valor] = Vertices(valor)

	def get_vertice(self,valor):
		
		if valor not in self.vertices:

			self.add_vertice(valor)

		return self.vertices[valor] 

	def get_proxima_palavra(self , palavra_atual):
		return self.vertices[palavra_atual.valor].proxima_palavra()

	def gera_mapa_de_probabilidade(self):
		
		for vertice in self.vertices.values():
			vertice.get_mapa_probabilidade()