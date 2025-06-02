# Seletor de opções inseguro

print("Selecione uma opção de suco de frutas [-1 para sair]:")
opcoes = ['maçã', 'laranja', 'uva']
while True:
	print(f"Digite um número inteiro para selecionar.")
	print(opcoes, '\n')
	opidx = int(input("$: "))
	if opidx == -1: break
	print(f"Você selecionou: {opcoes[opidx]}\n\n")
	break

