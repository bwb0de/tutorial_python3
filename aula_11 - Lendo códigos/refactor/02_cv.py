def estimar_consumo_veicular():
	distancia = float(input("Informe a distancia desejada: "))
	velocidade = float(input("Informe a velocidade media: "))
	tempo_medio_viagem = calcular_tempo_medio_da_viagem_como_decimal(distancia, velocidade)
	taxa_consumo = ajustar_taxa_de_consumo_conforme_a_velocidade(velocidade)
	litros_consumidos = calcular_quantidade_litros_consumidos(distancia, taxa_consumo)
	tempo_formato_acessivel = converter_tempo_medio_para_tempo_aproximado_formato_acessivel(tempo_medio_viagem)
	imprimir_resultado(distancia, velocidade, tempo_formato_acessivel, litros_consumidos)
	
	


def calcular_tempo_medio_da_viagem_como_decimal(distancia, velocidade):
	return distancia / velocidade
	
	

def converter_tempo_medio_para_tempo_aproximado_formato_acessivel(tempo_medio_viagem):
	tempo_formato_acessivel = str(int(tempo_medio_viagem))+'h' #Inicializando com parte inteira apenas
	tempo_parte_decimal = tempo_medio_viagem - int(tempo_medio_viagem)
	
	#Complementa a informação de tempo_formato_acessivel pela análise da parte decimal
	if 0.0 <= tempo_parte_decimal <= 0.25:
		tempo_formato_acessivel += '15m'
	elif 0.25 < tempo_parte_decimal <= 0.50:
		tempo_formato_acessivel += '30m'
	elif 0.50 < tempo_parte_decimal <= 0.75:
		tempo_formato_acessivel += '45m'
	elif 0.75 < tempo_parte_decimal <= 1.0:
		tempo_formato_acessivel = str(int(t)+1)+'h' #Redefine e erredonda para cima a parte inteira
	
	return tempo_formato_acessivel



def ajustar_taxa_de_consumo_conforme_a_velocidade(velocidade):
	#Obs: esta função poderia ser abstraída para receber os parâmetros de consumo conforme o veículo
	
	consumo = 12.5 #Representa a distancia [km] por litro [L]

	if velocidade <= 60:
		consumo = 14.2
	elif 60 <= velocidade < 80:
		consumo = 13.8
	elif 80 <= velocidade < 93:
		consumo = 12.5
	elif 93 <= velocidade < 110:
		consumo = 11.3
	elif velocidade >= 110:
		consumo = 10.1		
	
	return consumo
	
	
def calcular_quantidade_litros_consumidos(distancia, consumo):
	return distancia / consumo



def imprimir_resultado(distancia, velocidade, tempo, litros):
	msg  = f"Para percorrer {distancia:.2f}km com velocidade {velocidade:.2f}km/h "
	msg += f"você leverá aproximadamente {tempo} "
	msg += f"e consumirá {litros:.2f}L de combustível..."
	print(msg)



if __name__ == "__main__":
	estimar_consumo_veicular()
