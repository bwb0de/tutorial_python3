#
# Faça um programa que receba a data de nascimento de uma pessoa, calcule a idade dela
# e indique se ela tem idade suficiente para dirigir um carro.
#
# Não modifique o código inicialmente fornecido, utilize os valores correntes de dia, 
# mes e ano em sua solução.
#

from datetime import datetime

hoje = datetime.today()

dia_corrente = hoje.day
mes_corrente = hoje.month
ano_corrente = hoje.year

dia, mes, ano = input("Informe adta de nascimento no formato DD/MM/AAAA: ").strip().split('/')
dia, mes, ano = int(dia), int(mes), int(ano)

idade_prevista = ano_corrente - ano

if mes_corrente < mes or ((mes_corrente == mes) and (dia_corrente < dia)):
    print(f"Idade da pessoa é: {idade_prevista - 1}")
else:
    print(f"Idade da pessoa é: {idade_prevista}")
