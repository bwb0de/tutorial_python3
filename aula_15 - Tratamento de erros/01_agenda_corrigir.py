#
# Esta é uma versão possível do programa de agenda proposto na aula anterior...
# Seria um programa utilizável se não existissem tantos erros...
#
# Corrija os 9 erros que existem no código para obter um programa funcional.
#
# Dica: alguns erros são explícitos, outros são mais sutis e levam a comportamentos
# inesperados. Pode ser necessário verificar, eventualmente, o conteúdo do
# arquivo de dados para compreender o que ocorre.
#


ARQUIVO = "agenda_db.txt"


def executor_acoes():
    print(MENU)
    print("1: criar um registro")
    print("2: ler registros")
    print("3: sair\n")
    opcao = input("Escolha um número: ")
    print("")

    if opcao == '1':
        novo_evento = criar_registro()
        gravar_evento(novo_evento)
        print("")
    elif opcao == 2:
        dados_convertidos = ler_eventos()
        for evento in dados_convertidos:
            print("{evento['data']}:", evento['descricao'])
        print("")
    elif opcao = '3':
        exit
    else:
        print("Opção desconhecida...\n")


def criar_registro() -> dict:
    data = input("Data do evento: ")
    descricao = input("Descrição: ")
    evento = 'data:::{data};;;descricao:::{descricao}\n' 
    return evento


def gravar_evento(evento, nome_arquivo=ARQUIVO) -> None:
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(evento)
    arquivo.close()


def conversor_formato(dados_arquivo_db) -> list:
    dados_pre_convertidos = dados_arquivo_db.split('\n')
    dados_convertidos = []
    for linha in dados_pre_convertidos:
        campos = linha.strip().split(';;;')
        evento_convertido = {}
        for i, campo in enumerate(campos):
            k, v = campo.split(':::')
            evento_convertido[k] = v
        dados_convertidos.append(evento_convertido)
    return dados_convertidos


def ler_eventos(nome_arquivo, conversor=conversor_formato) -> list:
    arquivo = open(nome_arquivo)
    dados = arquivo.read()
    arquivo.close()
    dados_convertidos = conversor(dados)
    return dados_convertidos



def main():
    while True:
        executor_acoes()
    

if __name__ == '__main__':
    main()
