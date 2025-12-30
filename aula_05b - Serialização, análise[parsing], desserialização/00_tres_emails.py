#
# Faça um programa que imprima os três primeiros endereços
# de email registrados no arquivo "dados_participantes.txt"
#

f = open("dados_participantes.txt")

linha = f.readline()
email = linha.split(";;")[-1].strip()
print(email)

linha = f.readline()
email = linha.split(";;")[-1].strip()
print(email)

linha = f.readline()
email = linha.split(";;")[-1].strip()
print(email)

f.close()
