#
# Crie um programa que recebe a uma string de tempo no formato 00h00m00s
# e imprima o tempo em segundos.
#

string_tempo = input("Informe o tempo no formato ##h##m##s: ")
string_tempo = string_tempo.strip().replace('h','s').replace('m','s').split('s')
horas, minutos, *segundos = string_tempo

print(f'O tempo em segundos equivale a: {(int(horas)*60*60)+(int(minutos)*60)+int(segundos[0])}')
