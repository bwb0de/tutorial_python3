#
# Crie um jogo de adivinhação. O usuário deve fornecer números entre 
# 0 e 100 na tentativa de descobrir qual o número sorteado. O programa 
# deve fornecer informações ao usuário a cada tentativa. Se, 
# por exemplo, o número digitado pelo usuário for maior que o número 
# sorteado, o programa deve indicar que o valor do número sorteado é 
# menor que o informado. O mesmo se aplica para situação inversa. 
# Se o usuário acertar o número apresente uma mensagem de congratulação 
# na linha de comando e finalize o programa.
#
# Dica: use o módulo random
#

import random

numero_sorteado = random.randint(0,100)

print("Adivinhe qual número foi sorteado entre 0-100:")
while True:
	tentativa = int(input('$:'))
	if tentativa == numero_sorteado:
		print("\nParabéns! Você acertou!\n")
		break
	elif tentativa < numero_sorteado:
		print('\nVocê errou... O número é maior...\n')
	elif tentativa > numero_sorteado:
		print('\nVocê errou... O número é menor...\n')


	
