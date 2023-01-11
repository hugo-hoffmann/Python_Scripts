import random
import string

def wordlist_organizada():

	wordlist = []
	with open('lista de palavras pt-br.txt' , 'r+') as arquivo:

		for palavra in arquivo:

			wordlist.append(palavra.strip())


	return wordlist

wordlist_organizada()

def jogo_da_forca():

	wordlist = wordlist_organizada()
	word = random.choice(wordlist).upper()
	letras_da_palavra=set(word)
	alfabeto = set(string.ascii_uppercase)
	letras_usadas = set()
	vidas = 6

	while len(letras_da_palavra) > 0 and vidas > 0:
		
		print("Você tem", vidas, "restantes" "Você já escolheu essas letras: ", ' '.join(letras_usadas))
		palavra_em_jogo = [letra if letra in letras_usadas else '-' for letra in word]
		print("Palavra: " , ' '.join(palavra_em_jogo))

		letra_do_usuario = input("Digite uma letra: ").upper()

		if letra_do_usuario in alfabeto - letras_usadas:

			letras_usadas.add(letra_do_usuario)

			if letra_do_usuario in letras_da_palavra:

				letras_da_palavra.remove(letra_do_usuario)
			else:

				vidas = vidas -1
				print("A letra escolhida não está na palavra!")
				

		elif letra_do_usuario in letras_usadas:
			print ("Você já usou essa letra!")

		else:
			print("Caractere inválido!")

	if vidas == 0:
		print("Você perdeu! A palavra era", word )

	else:

		print("Você adivinhou a palavra!")


jogo_da_forca()
