#
# Obter três multiplos de 13 aleatoriamente
#

import random

resposta = []
numero_tentativas = 0
while len(resposta) != 3:
	numero_aleatorio = random.randint(1,1001)
	if (numero_aleatorio) % 13 == 0:
		resposta.append(numero_aleatorio)
	numero_tentativas += 1

print(resposta)
print("número de tentativas:", numero_tentativas)
