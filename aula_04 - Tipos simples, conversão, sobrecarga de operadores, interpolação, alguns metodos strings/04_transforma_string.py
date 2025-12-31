#
# Crie um programa que receba uma frase e retorne uma versão transformada dessa 
# frase substituindo todos os espaços por “_” e colocando todas as letras em minúsculo.
#

frase = input("Escreva uma frase, aperte ENTER para enviar: ")
frase_transformada = frase.lower().strip().replace(" ","_")
print(frase_transformada)
