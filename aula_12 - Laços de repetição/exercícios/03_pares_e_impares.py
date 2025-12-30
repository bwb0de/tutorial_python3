#
# Faça um programa que avalie uma sequência de numeros inteiros informando:
#    - o total de números da sequencia
#    - a quantidade de números pares
#    - a quantidade de números ímpares
#

import random
numeros = [random.randint(0,1000) for _ in range(random.randint(200,500))]

def numero_par(n):
    return n % 2 == 0


n_elementos = 0
n_elementos_pares = 0
n_elementos_impares = 0
for n in numeros:
    n_elementos += 1
    if numero_par(n):
        n_elementos_pares += 1
    else:
        n_elementos_impares += 1


print("Resumo:")
print("  -total elementos:", n_elementos)
print("  -total pares:", n_elementos_pares)
print("  -total impares:", n_elementos_impares)


