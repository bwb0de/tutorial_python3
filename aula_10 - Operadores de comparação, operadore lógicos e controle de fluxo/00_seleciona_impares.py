#
# Implemantar uma função que seleciona apenas os números ímpares de uma lista
# de sete numeros fornecidos pelo usuário
#

selecionados = []

n1 = int(input("1º Número: "))
n2 = int(input("2º Número: "))
n3 = int(input("3º Número: "))
n4 = int(input("4º Número: "))
n5 = int(input("5º Número: "))
n6 = int(input("6º Número: "))
n7 = int(input("7º Número: "))

if n1 % 2 != 0: selecionados.append(n1)
if n2 % 2 != 0: selecionados.append(n2)
if n3 % 2 != 0: selecionados.append(n3)
if n4 % 2 != 0: selecionados.append(n4)
if n5 % 2 != 0: selecionados.append(n5)
if n6 % 2 != 0: selecionados.append(n6)
if n7 % 2 != 0: selecionados.append(n7)

print("Os números ímpares são:", selecionados)

