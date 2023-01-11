import random

def palpite(x):

	random_number = random.randint(1,x)
	palpite = 0

	while palpite != random_number:

		palpite = int(input(f"Digite um número entre 1 e {x}: "))
		if palpite < random_number:
			print("Você digitou um valor muito baixo!")

		elif palpite > random_number:

			print("Você digitou um valor muito alto!")
	print (f"Você acertou o número {random_number}" )

palpite(10)