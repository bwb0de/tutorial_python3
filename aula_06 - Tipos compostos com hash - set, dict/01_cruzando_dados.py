#
# Crie um programa que leia dois arquivos de lista e identifique os 
# elementos comuns aos dois arquivos.
#
# Dica: usar métodos de string e sets
#

arquivo1 = open('l1.txt')
dados_arquivo1 = arquivo1.read().strip().split('\n')
dados_arquivo1 = set(dados_arquivo1)
arquivo1.close()

arquivo2 = open('l2.txt')
dados_arquivo2 = arquivo2.read().strip().split('\n')
dados_arquivo2 = set(dados_arquivo2)
arquivo2.close()

print("Elementos comuns aos dois arquivos:", list(dados_arquivo1.intersection(dados_arquivo2)))
