#
# Crie um programa que calcule a quantidade de tinta necessária para pintar as paredes
# de uma casa ou prédio
#
# Informações relevantes:
#  - altura do pé direito
#  - soma da metragem linear das paredes
#  - uma lata de tinta pinta 2.25 m² de parede
#  - desconte a área de portas e janelas 
#  - assuma que todas portas e janelas tem o mesmo tamanho
#

AREA_PINTURA_POR_LATA = 2.25

pe_direito = float(input("Altura do pé direito em metros: ").replace(",","."))
comprimento_linear_paredes = float(input("Soma do comprimento linear das paredes em metros: ").replace(",","."))

janela_largura = float(input("Largura janela em metros: ").replace(",","."))
janela_altura = float(input("Altura janela em metros: ").replace(",","."))
janela_qtd = int(input("Número de janelas na área a ser pintada: "))

porta_largura = float(input("Largura porta em metros: ").replace(",","."))
porta_altura = float(input("Altura porta em metros: ").replace(",","."))
porta_qtd = int(input("Número de portas na área a ser pintada: "))

area_inicial = pe_direito * comprimento_linear_paredes
area_descontada_janelas = janela_largura * janela_altura * janela_qtd
area_descontada_portas = porta_altura * porta_largura * porta_qtd

area_pintura = area_inicial - (area_descontada_janelas + area_descontada_portas)

qtd_latas = area_pintura / AREA_PINTURA_POR_LATA
print(f"Valor calculado: {qtd_latas}")
print(f"Serão necessárias {int(qtd_latas)+1} latas de tinta...")


