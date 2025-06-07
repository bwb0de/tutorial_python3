#
# Crie um programa em que o usuário digita 3 números inteiros em 
# uma mesma linha e o programa imprime a média aritmética entre os
# números digitados.
#
# Dica: use packing e metodos de strings para isolar os numeros
#

numeros_string = input("Digite 3 números inteiros separados por espaço: ").strip().split()
n1, n2, n3 = numeros_string
n1, n2, n3 = int(n1), int(n2), int(n3)

media = (n1 + n2 + n3) / 3

print(f"O valor médio entre os números digitados é: {media}")
