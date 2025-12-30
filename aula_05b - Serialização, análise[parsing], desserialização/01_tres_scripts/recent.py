f = open("base_dados.txt")
dados = f.read(); f.close()
dados = dados.replace('--', '\t').split('\n')
print(*dados[-4:], sep='\n')

