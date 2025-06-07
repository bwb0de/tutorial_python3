#
# Crie um programa que receba do usuário um número real/decimal e imprima na tela
# o triplo e a metade do valor inicialmente fornecido.
#

numero_str = input("Informe um númro real: ")
numero_str = numero_str.replace(",",".")
numero_real = float(numero_str)

triplo = numero_real * 3
metade = numero_real / 2

print(f"O triplo de {numero_real} é {triplo} e a metade é {metade}")
