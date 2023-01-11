import random
import math

class Player:

	def __init__(self, letra):
		#letra é x ou o
		self.letra = letra

	def movimento(self,jogo):

		pass

	class RandomComputerPlayer(Player):

		def __init__(self,letra):

			super().__init__(letra)

		def movimento(self,jogo):

			quadrado = random.choice(game.movimentos_disponiveis())
			return quadrado

		class HumanPlayer(Player):

			def __init__(self,letra):

				super().__init__(letra)

			def movimento(self,jogo):

				quadrado_valido = false
				val = None
				square = input(self.letra + "Digite a casa desejada para fazer o movimento: ")

				try:

					val = int(quadrado)

					if val not in jogo.movimentos_disponiveis():

						raise ValueError
					quadrado_valido = True

				except ValueError:
					print("Quadrado Inválido. Tente novamente.")

				return val  