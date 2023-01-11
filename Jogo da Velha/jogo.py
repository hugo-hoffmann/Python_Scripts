from player import HumanPlayer , RandomComputerPlayer

class Jogo_da_Velha:
	"""docstring for Jogo da Velha"""
	def __init__(self):
		self.tabuleiro = [' ' for _ in range(9)]
		self.vencedor = None

	def print_tabuleiro(self):

		for row in [self.tabuleiro[i*3:(i+1)*3] for i in range(3)]:
			print('| ' + ' | '.join(row) + ' |')

	@metodo_estatico

	def print_num_tabuleiro():

		num_tabuleiro = [[str(i) for i in range((j*3), (j+1)*3)] for j in range(3)]

		for row in num_tabuleiro:
			print('| ' + ' | '.join(row) + ' |')

	def movimentos_disponiveis(self):

		movimentos =[]
		
		for (i,spot) in enumerate(self.tabuleiro):

			if spot == ' ':

				movimentos.append(i)

		return movimentos 

	def quadrado_vazio(self):
		return ' ' in self.tabuleiro

	def num_quadrados_vazios(self):

		return len(self.movimentos_disponiveis())

	def make_move(self, quadrado, letra):

		if self.tabuleiro[quadrado] == ' ':
			self.tabuleiro[quadrado]= letra
			if self.vencedor(quadrado,letra):
				self.vencedor = letra
			return True
		return False

	def vencedor(self,quadrado,letra):
		row_ind = quadrado // 3
		row = self.tabuleiro[row_ind*3 : (row_ind +1)*3]

		if all([spot == letra for spot in row]):
			return True

		col_ind = quadrado %3
		coluna = [self.tabuleiro[col_ind+i*3] for i in range(3)]

		if all(spot == letra for spot in coluna):
			return True

		if quadrado % 2 == 0:
			diagonal_1 = [self.tabuleiro[i] for i in [0,4,8]]
			diagonal_2 = [self.tabuleiro[i] for i in [2,4,6]]

			if all(spot == letra for spot in diagonal_1):
				return True
			if all(spot == letra for spot in diagonal_2):
				return True

		return False


def  partida(jogo, jogador_x , jogador_o , print_jogo = True):

	if print_jogo:
		jogo.print_num_tabuleiro()

	letra = 'X'

	while jogo.quadrado_vazio():

		if letra == 'O':
			quadrado = jogador_o.movimento(jogo)

		else:
			quadrado = jogador_x.movimento(jogo)
	
		if jogo.make_move(quadrado,letra):
			if print_jogo:
				print(letra + f'faça o movimento no quadrado {quadrado}')
				jogo.print_tabuleiro()
				print(' ')
			if jogo.vencedor:
				if print_jogo:
					print(letra + 'venceu!')

			letra ='O' if letra =='X' else 'X'

	if print_jogo:

		print("Empate!")

if __name__ == '__main__':
	jogador_x = HumanPlayer('X')
	jogador_o = RandomComputerPlayer('O')
	j = Jogo_da_Velha()
	partida(jogador_x,jogador_o,print_jogo=True)