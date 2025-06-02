# Seletor de opções seguro

print("Selecione uma opção de suco de frutas [-1 para sair]:")
opcoes = ['maçã', 'laranja', 'uva']
while True:
	try:
		print(f"Digite um número inteiro para selecionar.")
		print(opcoes, '\n')
		opidx = int(input("$: "))
		if opidx == -1: break
		print(f"Você selecionou: {opcoes[opidx]}\n\n")
		break
	
	
	except IndexError:
		print(f"\nVocê digitou um índice inválido, o valor deve estar entre 0 e {len(opcoes) - 1}...\n")
		continue
	except ValueError:
		print(f"\nO valor fornecido precisa ser numérico, digite -1 se quiser encerar o programa...\n")
		continue
	except KeyboardInterrupt:
		print(f"\nPrograma finalizado [Ctrl+C]...")
		break

