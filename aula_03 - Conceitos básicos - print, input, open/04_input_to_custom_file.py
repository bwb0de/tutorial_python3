#
# Crie um programa que leia um valor fornecido pelo usuário e escreva o
# resultado em um arquivo de destino com nome também indicado pelo
# usuário.
#


informacao = input("Informação a ser gravada: ")
nome_novo_arquivo = input("Nome do arquivo de destino: ")
arquivo = open(nome_novo_arquivo, 'w')
arquivo.write(informacao)
arquivo.close()
