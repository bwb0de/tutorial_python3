# Implemantar função que calcula o IMC de uma pessoa.
#
# IMC é uma sigla utilizada para Índice de Massa Corporal.
#
# O Índice de Massa Corporal é uma medida utilizada para medir a obesidade
# adotada pela Organização Mundial de Saúde (OMS). É o padrão internacional
# para avaliar o grau de obesidade.
#
# O IMC de uma pessoa pode ser calculado pela formula: peso / altura².
#
# Em seguida esse índice é comparado com uma tabela de intervalos para
# identificar a situação da pessoa em relação ao seu peso corporal
#
# Se IMC:
#	- abaixo de 17 => Muito abaixo do peso
# 	- entre 17 e 18,49 => Abaixo do peso
# 	- entre 18,5 e 24,99 =>	Peso normal
# 	- entre 25 e 29,99 => Acima do peso
# 	- entre 30 e 34,99 => Obesidade I
# 	- entre 35 e 39,99 => Obesidade II (severa)
# 	- acima de 40 => Obesidade III (mórbida)
#
# Dica: utilizar a função round indicando o número de casas decimais 2

altura = float(input("Informe o valor da altura em metros: "))
peso = float(input("Informe o valor do peso em kilogramas: "))

imc = peso / (altura ** 2)
imc = round(imc,2)

if imc < 17.00: 
    print("Muito abaixo do peso.")
elif 17.00 <= imc <= 18.49: 
    print("Abaixo do peso.")
elif 18.50 <= imc <= 24.99: 
    print("Peso normal.")
elif 25.00 <= imc <= 29.99: 
    print("Acima do peso.")
elif 30.00 <= imc <= 34.99: 
    print("Obesidade I.")
elif 35.00 <= imc <= 39.99: 
    print("Obesidade II (severa).")
elif imc >= 40.00: 
    print("Obesidade III (mórbida).")
