#
# Faça um programa que calcule o custo de uma viagem em reais. O custo cobrado
# por quilometro é de R$0.70, contudo, para viagem superiores a 150km o custo
# aumenta em 13%
#
# Apresente o valor final arredondado, com apenas duas casas decimais...
#

CUSTO_PADRAO = 0.70
CUSTO_AUMENTADO = CUSTO_PADRAO * 1.13

distancia_viagem = float(input("Informe a distância total da viagem em quilometros: "))

if distancia_viagem > 150.0:
    custo_final = distancia_viagem * CUSTO_AUMENTADO
    print(f"O custo final para essa viagem é R${round(custo_final,2):.2f}")
else:
    custo_final = distancia_viagem * CUSTO_PADRAO
    print(f"O custo final para essa viagem é R${round(custo_final,2):.2f}")


