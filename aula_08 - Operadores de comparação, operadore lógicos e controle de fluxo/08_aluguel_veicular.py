#
# Uma empresa de aluguel de veículos trabalha com os os seguintes critérios:
#   - custo diário carro popular => R$112,00
#   - custo diário SUV => R$175,00
#   - custo diário minivan => R$210,00
#
# Além disso, há uma cobrança adicional relacionada à quilometragem de R$0,10 
# por quilometro rodado ou R$0,07 se a quilometragem total utilizada ultrapassar 250km
#
# For fim, podem ser cobrados valores adicionais caso o carro seja devolvido sujo
# ou caso o cliente solicite cadeirinha infantil, respectivamente os valores são:
# R$45,00 e R$70,00
#
# Caso o pagamento seja feito em dinheiro vivo ou pix (à vista) há um desconto de 7%.
#
# Crie um programa que calcule o custo final de aluguel do veículo conforme as opções
# selecionadas e apresente um relatório detalhado para ciência do cliente. Apresente
# no relatório apenas informações relevantes para o cliente em questão...
#
# Não permita que o programa prossiga se forem informadas opções inadequadas...
#


custo_diario_veiculo = 0
custo_quilometragem = 0.10

CUSTO_LIMPEZA = 45.00
CUSTO_CADEIRINHA = 70.00

adicional_limpeza = 0
adicional_cadeirinha = 0

print("Cálculo do custo de locação do veículo...\n")
print("Indique qual foi o ripo de veículo alugado:")
print("1: Carro popular")
print("2: SUV")
print("3: Minivan")
opcao_veiculo = int(input('[1-3]: '))

if opcao_veiculo < 1 or opcao_veiculo > 3:
    print("\nOpção invalida! Você deve escolher um dos números: 1, 2 ou 3")
    exit()
elif opcao_veiculo == 1:
    custo_diario_veiculo = 112.00
elif opcao_veiculo == 2:
    custo_diario_veiculo = 175.00
elif opcao_veiculo == 3:
    custo_diario_veiculo = 210.00

numero_dias = int(input("\nInforme o número de dias que o carro foi alugado [1+]: "))

if numero_dias < 0:
    print("\nValor inválido, dias deve ser um número positivo...")
    exit()

distancia_percorrida = float(input("\nInforme a quilometragem [0.00+]: ").replace(",","."))

if distancia_percorrida <= 0:
    print("\nValor informado incorreto! Você deve fornecer um número positivo...")
    exit()
elif distancia_percorrida > 250:
    custo_quilometragem = 0.07

print("\nO carro foi devolvido limpo:")
print("1: Sim")
print("2: Não")
adicional_limpeza = (int(input('[1-2]: ')) - 1) * CUSTO_LIMPEZA

if adicional_limpeza < 0.0 or adicional_limpeza > CUSTO_LIMPEZA:
    print("\nOpção invalida! Você deve escolher um dos números: 1 ou 2")
    exit()

print("\nO cliente solicitou cadeirinha:")
print("1: Não")
print("2: Sim")
adicional_cadeirinha = (int(input('[1-2]: ')) - 1) * CUSTO_CADEIRINHA

if adicional_cadeirinha < 0.0 or adicional_cadeirinha > CUSTO_CADEIRINHA:
    print("\nOpção invalida! Você deve escolher um dos números: 1 ou 2")
    exit()

custo_locacao = (custo_diario_veiculo * numero_dias)
custo_adicional_quilometragem = custo_quilometragem * distancia_percorrida
custo_final = custo_locacao + custo_adicional_quilometragem + adicional_limpeza + adicional_cadeirinha

print('\n\n' + '='*45)
print(f"\nO custo final é R${custo_final:.2f}")
print(f" -custo base: {custo_diario_veiculo:.2f}[veiculo/dia] * {numero_dias}[dias] = R${custo_locacao:.2f}")
print(f" -custo quilometragem: {distancia_percorrida}[distancia] * {custo_quilometragem}[$/km] = R${custo_adicional_quilometragem:.2f}")
if adicional_limpeza:
    print(f" -custo adicional limpeza veicular: R${adicional_limpeza:.2f}...")
if adicional_cadeirinha:
    print(f" -custi adicional locação cadeirinha: R${adicional_cadeirinha:.2f}...\n\n")


