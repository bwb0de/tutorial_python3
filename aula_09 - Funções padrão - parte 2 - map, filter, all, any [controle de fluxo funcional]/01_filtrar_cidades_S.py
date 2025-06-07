# 
# Criar programa que leia o arquivo 'cidades.txt' e selecione e imprima
# aquelas que tenham a letra ‘S’ letra inicial
#

def selecionar_cidades_com_S_inicial(cidade):
    return cidade[0] == 'S'

arquivo = open('cidades.txt')
conteudo_do_arquivo = arquivo.read().strip().split('; ')
cidades_selecionadas = tuple(filter(selecionar_cidades_com_S_inicial, conteudo_do_arquivo))
arquivo.close()

print("As cidades com a inicial 'S' são:", *cidades_selecionadas, sep='\n')
