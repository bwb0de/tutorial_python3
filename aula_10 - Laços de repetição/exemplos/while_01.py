print("Digite 0 ou um valor negativo para finalizar o programa...")
total_compras = 0.0
preco = input('Preço no formato [#.##]: ').strip()
while float(preco) > 0.0:
    total_compras += float(preco)
    preco = input('Preço no formato [#.##]: ').strip()
    
print("Total:", total_compras)
