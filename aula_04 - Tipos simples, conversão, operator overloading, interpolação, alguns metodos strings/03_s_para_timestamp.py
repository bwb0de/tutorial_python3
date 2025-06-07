#
# Crie um programa que receba um número em segundos e imprima uma
# informação com a representação desse tempo convertido no formato 
# 00h00m00s.
#

segundos = int(input("Informe uma quantidade em segundos: "))

horas = (segundos // 60) // 60
segundos = segundos - (horas * 60 * 60)
minutos = segundos // 60
segundos = segundos - (minutos * 60)

print(f'Isso equivale a {str(horas).zfill(2)}h{str(minutos).zfill(2)}m{str(segundos).zfill(2)}s...')
