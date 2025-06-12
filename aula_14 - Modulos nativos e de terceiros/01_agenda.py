#
# Crie um programa que funciona como uma agenda. Os dados de registro são data do evento, descrição e prioridade.
#
# O programa deve possuir um menu com opções:
#   1 – registrar evento/compromisso
#   2 – apagar evento/compromisso
#   3 – listar registros
#   4 – sair 
#
# Dica: use estruturas como dicionários e listas. Use o módulo json para persistir os dados a cada inclusão ou retirada
#


import json
from pathlib import Path

ARQUIVO_AGENDA = 'agenda.json'

class DataBR:
    def __init__(self, data_br: str):
        dia, mes, ano = data_br.strip().split('/')
        dia, mes, ano = int(dia), int(mes), int(ano)

        ano_bisexto = False #self.ano_bisexto(ano)

        if any([dia < 0, mes < 0, ano < 0, mes > 12]):
            raise ValueError("Data fornecida parece inadequada...")

        elif mes in {1, 3, 5, 7, 8, 10, 12} and dia > 31:
            raise ValueError("Data fornecida parece inadequada...")

        elif mes in {4, 6, 9, 11} and dia > 30:
            raise ValueError("Data fornecida parece inadequada...")

        elif mes == 2 and ano_bisexto and dia > 29:
            raise ValueError("Data fornecida parece inadequada...")

        elif mes == 2 and not ano_bisexto and dia > 28:
            raise ValueError("Data fornecida parece inadequada...")

        self.__ano = ano
        self.__mes = mes
        self.__dia = dia

    def __eq__(self, other):
        return all([
            self.dia == other.dia,
            self.mes == other.mes,
            self.ano == other.ano
        ])

    def __lt__(self, other):
        return any([
            self.ano < other.ano,
            self.ano == other.ano and self.mes < other.mes,
            self.ano == other.ano and self.mes == other.mes and self.dia < other.dia
        ])

    def __gt__(self, other):
        return any([
            self.ano > other.ano,
            self.ano == other.ano and self.mes > other.mes,
            self.ano == other.ano and self.mes == other.mes and self.dia > other.dia
        ])

    def __str__(self):
        return f'br[{str(self.dia).zfill(2)}/{str(self.mes).zfill(2)}/{str(self.ano).zfill(4)}]'

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes
   
    @property
    def ano(self):
        return self.__ano



def criar_arquivo_agenda(arquivo_eventos):
	arquivo = Path(arquivo_eventos)
	if arquivo.exists():
		return
	arquivo = open(str(arquivo), 'w')
	arquivo.write(json.dumps([]))
	arquivo.close()


def registrar_evento(eventos):
	data = input("Data do evento [DD/MM/AAAA]: "); validate = DataBR(data)
	info = input("Descrição evento: ")
	prioridade = int(input("Prioridade [1-5]: "))

	evento = {
		'data': data,
		'info': info,
		'prioridade': prioridade
	}

	eventos.append(evento)
	del(validate)
	return eventos



def gravar_eventos(eventos, arquivo_eventos):
	arquivo = open(arquivo_eventos, 'w')
	conteudo = arquivo.write(json.dumps(eventos))
	arquivo.close()



def ler_eventos(arquivo_eventos):
	arquivo = open(arquivo_eventos)
	conteudo = arquivo.read()
	arquivo.close()
	conteudo = json.loads(conteudo)
	return conteudo


def ler_e_mostrar_eventos(arquivo_eventos, como_menu=False):
	eventos_base = ler_eventos(arquivo_eventos)

	if len(eventos_base) == 0:
		print("Não há eventos registrados...")
		return []

	eventos = [(DataBR(e['data']), e['info'], int(e['prioridade'])) for e in eventos_base]
	eventos.sort(key=lambda x: x[0])
	if como_menu: print("Selecione os eventos pelo número:")
	n = 0
	for e in eventos:
		n += 1
		if como_menu:
			print(f"{n}: {e[1]} ({e[0]})")
			continue
		print(*e, sep='\n')
		print("")
	return eventos


def apagar_eventos(eventos_apagar: set, arquivo_eventos: str):
	eventos = ler_eventos(arquivo_eventos)
	for idx in range(len(eventos)-1, -1, -1):
		if eventos[idx]['info'] in eventos_apagar:
			_ = eventos.pop(idx)
	return eventos
	


def main():
	criar_arquivo_agenda(ARQUIVO_AGENDA)
	while True:
		# ----- Menu -----
		print("")
		print("Escolha uma opção:")
		print("1: Registrar evento/compromisso")
		print("2: Listar registros")
		print("3: Apagar registros")
		print("4: Sair")
		op = int(input("$: "))
		print("")

		if op > 4 or op < 1:
			print("\nOpção inválida!\n")
			continue

		if op == 4:
			print("")
			break

		elif op == 1:
			eventos = ler_eventos(ARQUIVO_AGENDA)
			eventos = registrar_evento(eventos)
			gravar_eventos(eventos, ARQUIVO_AGENDA)

		elif op == 2:
			eventos = ler_e_mostrar_eventos(ARQUIVO_AGENDA)
			if eventos == []:
				continue
			input('Pressine ENTER para continuar...')
	
		elif op == 3:
			eventos = ler_e_mostrar_eventos(ARQUIVO_AGENDA, como_menu=True)
			if eventos == []:
				continue
			nums = input("$: ").strip().split(",")
			nums = [int(n)-1 for n in nums]  #convertendo seleção para indices da lista
			eventos_apagar = set()
			for idx in nums:
				eventos_apagar.add(eventos[idx][1])
			eventos = apagar_eventos(eventos_apagar, ARQUIVO_AGENDA)
			gravar_eventos(eventos, ARQUIVO_AGENDA)
			

if __name__ == '__main__':
	main()



				




