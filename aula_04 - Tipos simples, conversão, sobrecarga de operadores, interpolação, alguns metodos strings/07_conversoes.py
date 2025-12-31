#
# Crie um programa que receba um valor em reais e apresente na tela o valor
# convertido em três moedas diferentes
#

valor_reais = float(input("Digiter um valor em R$: ").replace(",","."))

tx_USD  = 5.863 # dolar turismo
tx_PARG = 0.005 # peso argentino
tx_EUR  = 6.430 # euro

print("O valor apresentado corresponde a:")
print(f"- US$ {valor_reais / tx_USD}, dolares americanos")
print(f"- US$ {valor_reais / tx_PARG}, pesos argentinos")
print(f"- EU$ {valor_reais / tx_EUR}, euros")
