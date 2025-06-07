#
# Crie um programa que receba um valor e escreva o valor em um arquivo 
# 'meus_dados.txt'
#

arquivo = open('meus_dados.txt', 'w')
arquivo.write(input("Digite algo: "))
arquivo.close()
