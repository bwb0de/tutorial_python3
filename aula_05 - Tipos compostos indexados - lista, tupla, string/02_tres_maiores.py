#
# Crie um programa que recebe 5 números do usuário e imprima na tela
# os três maiores.
#

lista_numeros = []

n1 = float(input("Informe o 1º número: ")); lista_numeros.append(n1)
n2 = float(input("Informe o 2º número: ")); lista_numeros.append(n2)
n3 = float(input("Informe o 3º número: ")); lista_numeros.append(n3)
n4 = float(input("Informe o 4º número: ")); lista_numeros.append(n4)
n5 = float(input("Informe o 5º número: ")); lista_numeros.append(n5)

lista_numeros.sort()
lista_numeros.reverse()

print("Os três maiores são:", lista_numeros[0:3])

