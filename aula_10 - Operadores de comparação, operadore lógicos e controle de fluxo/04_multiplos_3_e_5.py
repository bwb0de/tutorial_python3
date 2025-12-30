#
# Escreva um programa que receba um número inteiro do usuário. O programa deve
# informar se o numero recebido é, simultaneamente, um múltiplo de 3 e 5.
#

inteiro = int(input("Informe um número inteiro: "))

#Testes
multiplo_3 = inteiro % 3 == 0
multiplo_5 = not (inteiro % 5)

if multiplo_3 and multiplo_5:
    print("É simultaneamente múltiplo de 3 e 5...")
elif multiplo_5:
    print("É múltiplo de 5, mas não é de 3...")
elif multiplo_3:
    print("É múltiplo de 3, mas não é de 5...")
else:
    print("Não é múltiplo de 3 ou 5...")


