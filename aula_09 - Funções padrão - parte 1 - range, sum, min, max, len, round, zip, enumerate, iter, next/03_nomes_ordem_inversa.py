#
# Crie um programa que leia o arquivo 'nomes.txt' e ordene os registros 
# de forma inversa. Imprima todos os valores da lista, cada um em uma 
# linha.
#
# Dica: utilize print com unpacking e configure o separador para “\n”.
#

arquivo = open('nomes.txt')
conteudo_do_arquivo = arquivo.read().strip().split(",")
conteudo_do_arquivo.sort()
conteudo_do_arquivo.reverse()
arquivo.close()
print("Lista de nomes em ordem inversa:", *conteudo_do_arquivo, sep='\n')
