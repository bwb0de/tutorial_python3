# 
# Crie um programa que leia três inputs, respectivamente, horas, minutos
# e segundos, e indique a quantidade total em segundos correspondentes.
#

horas = int(input("Informe um valor inteiro de horas: "))
minutos = int(input("Informe um valor inteiro de minutos: "))
segundos = int(input("Informe um valor inteiro de segundos: "))

tempo_total_em_segundos = (60*60*horas) + (60*minutos) + segundos

print(f'O valor total convertido em segundos é: {tempo_total_em_segundos}')
