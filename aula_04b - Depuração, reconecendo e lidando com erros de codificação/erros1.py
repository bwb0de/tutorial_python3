valor fornecido = input(Digite seu nome:)
valor fornecido.uppercase()
ano_nascimento = input(Ano nascimento:)
ano_corrente = 2025
idade = ano_corrente - ano_nascimento
arquivo_registro = open("nomes_idades.txt')
arquivo.write(valor fornecido)
arquivo.write(idade)
arquivo.write(';')
arquivo.close()
print("Oi {valor fornecido}, sua idade é aproximadamente {idade} anos.")

