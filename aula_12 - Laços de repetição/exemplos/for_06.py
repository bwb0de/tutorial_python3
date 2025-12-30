produtos = (“Sabão”, “Arroz”, “Óleo”)
precos = (8.32, 16.55, 14.00)
for produto, preco in zip(produtos, precos):
	print(f“O produto {produto} custa {preco}”)
