#Pedra papel e tesoura

import random

def partida():
	jogador = input(" Qual a sua escolha? 'pe' para pedra, 'pa' para papel, 't' para tesoura\n")
	computador = random.choice(['pe', 'pa','t' ])

	if jogador == computador:

		return 'Empate!'
	if vencedor(jogador,computador):
		return 'Você Venceu!'

	return 'Você perdeu!'

def vencedor(jogador,oponente):
	
	if (jogador == 'pe' and oponente == 't') or (jogador == 't' and oponente == 'pa') \
	or (jogador == 'pa' and oponente == 'pe'):

		return True  
print(partida())