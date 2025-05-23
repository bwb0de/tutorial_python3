def distribuir_processos():
	lista_processos = obter_processos('p.txt')
	total_processos = len(lista_processos)
	lista_distribuida = separar_por_pessoa(lista_processos, 'Jussara', 'Antônio', 'Silvana')
	imprimir_lista_distribuída(lista_distribuida, total_processos)


def obter_processos(arquivo):
	f = open(arquivo, 'r')
	lista_processos = f.read().split()
	f.close()
	return lista_processos
	

def separar_por_pessoa(lista_processos, *pessoas): #Usando argumentos flexiveis *pessoas é entendido como uma tupla
	lista_distribuida = []
	for pessoa in pessoas:
		lista_distribuida.append([pessoa])
	for i, p in enumerate(lista_processos):
		dist_i = i % len(lista_distribuida)
		lista_distribuida[dist_i].append(p)
	return lista_distribuida


def imprimir_lista_distribuída(lista_ditribuida, total_processos):
	for subl in lista_ditribuida:
		pessoa = subl[0]
		processos = subl[1:]
		numero_processos = len(processos)
		print(f'{pessoa} [{numero_processos}]:')
		for p in processos:
			 print(f'  - {p}')
		print('\n')
	print(f'Total processos: {total_processos}')

if __name__ == "__main__":
	distribuir_processos()
