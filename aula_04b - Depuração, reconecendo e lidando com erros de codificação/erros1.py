valor_fornecido = input("Digite seu nome:")
valor_fornecido.upper()
ano_nascimento = input("Ano nascimento:")
ano_corrente = 2025
idade = ano_corrente - int(ano_nascimento)
arquivo_registro = open("nomes_idades.txt", 'a')
arquivo_registro.write(valor_fornecido+',')
arquivo_registro.write(str(idade))
arquivo_registro.write(';')
arquivo_registro.close()
print(f"Oi {valor_fornecido}, sua idade é aproximadamente {idade} anos.")

