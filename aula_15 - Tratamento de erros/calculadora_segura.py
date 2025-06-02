# Calculadora segura

print("Calculadora REPL, aperte Ctrl+C para finalizar o programa...")
while True:
	try:
		num1 = float(input("Digite o primeiro número: "))
		operacao = input("Digite a operação (+, -, *, /): ")
		num2 = float(input("Digite o segundo número: "))
		
		if operacao == '+':
			resultado = num1 + num2
		elif operacao == '-':
			resultado = num1 - num2
		elif operacao == '*':
			resultado = num1 * num2
		elif operacao == '/':
			resultado = num1 / num2
		else:
			print("Operação inválida!")
			continue
			
		print(f"Resultado: {num1} {operacao} {num2} = {resultado}\n\n")
		
	except ValueError:
		print("Erro: Digite apenas números válidos!")
	except ZeroDivisionError:
		print("Erro: Não é possível dividir por zero!")
	except KeyboardInterrupt:
		print("\nPrograma interrompido pelo usuário.")
		break
