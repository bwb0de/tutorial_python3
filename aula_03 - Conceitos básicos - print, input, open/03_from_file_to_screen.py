#
# Crie um programa que leia o conteúdo o arquivo 'dados.txt' e imprima 
# o conteúdo na tela.
#


arquivo = open('dados.txt')
conteudo_arquivo = arquivo.read()
arquivo.close()
print(conteudo_arquivo)
