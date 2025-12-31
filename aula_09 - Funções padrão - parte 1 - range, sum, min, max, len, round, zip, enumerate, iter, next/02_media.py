#
# Crie um programa que leia 7 números aleatórios digitados pelo usuário
# e mostre a média simples dos valores digitados.
#

sequencia = []

n1 = float(input("Informe o 1º número: ")); sequencia.append(n1)
n2 = float(input("Informe o 2º número: ")); sequencia.append(n2)
n3 = float(input("Informe o 3º número: ")); sequencia.append(n3)
n4 = float(input("Informe o 4º número: ")); sequencia.append(n4)
n5 = float(input("Informe o 5º número: ")); sequencia.append(n5)
n6 = float(input("Informe o 6º número: ")); sequencia.append(n6)
n7 = float(input("Informe o 7º número: ")); sequencia.append(n7)

media = sum(sequencia) / len(sequencia)

print("A média dos valores digitados é:", média)
