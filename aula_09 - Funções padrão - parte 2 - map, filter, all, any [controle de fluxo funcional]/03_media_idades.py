#
# Crie um programa que calcule a média de idade dos participantes listados
# no arquivo "dados_participantes.txt"
#


f = open("dados_participantes.txt")
dados = f.read().split('\n')[:-1]

def selecionar_data_nascimento(linha):
	return linha.split(";;")[1]


dados = list(map(selecionar_data_nascimento, dados))

def calcular_idade(dn):
	dia_hoje = 30
	mes_hoje = 12
	ano_hoje = 2025

	dia_dn, mes_dn, ano_dn = dn.split("/")
	dia_dn, mes_dn, ano_dn = int(dia_dn), int(mes_dn), int(ano_dn)

	valor_idade = ano_hoje - ano_dn

	if mes_dn < mes_hoje or (mes_dn == mes_hoje and dia_dn < dia_hoje):
		valor_idade -= 1
		return valor_idade

	return valor_idade


lista_idades = list(map(calcular_idade, dados))
media_idades = sum(lista_idades)/len(lista_idades)

print(lista_idades)
print(f"A média das idades é {media_idades}...")

