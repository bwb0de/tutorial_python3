nome = input("Nome: ")
dn = input("Data nascimento: ")
ocupacao = input("Ocupacao: ")
email = input("e-Mail: ")

f = open("base_dados.txt", "a")
f.write(f"{nome}--{dn}--{ocupacao}--{email}\n")
f.close()

print("Registro adicionado!!!")
