#
# Implemente uma função que receba dois valores inteiros e realize uma contagem
# regressiva. Os inteiros fornecidos podem ser de qualquer valor. O programa
# deverá identificar o maior valor entre os dois e adotálo como ponto de partida
# da contagem regressiva.
#
# Os números devem ser apresentados lado à lado separados por um ou dois espaços.
#
# Todos os números divisíveis por 7 que existirem na sequencia regressiva, devem 
# ser apresentados entre []. Ao final da sequência deve-se apresentar a mensagem
# concluído
#

def contagem_regressiva(n1, n2):
    if n1 > n2:
        maior = n1
        menor = n2
    elif n1 < n2:
        menor = n1
        maior = n2
    else:
        print('Não é possível formar sequência...')

    
    while maior != (menor - 1):
        if maior % 7 == 0:
            print(f"[{maior}]", end=" ")
        else:
            print(f"{maior}", end=" ")
        maior -= 1

    print("Concluído!")


contagem_regressiva(27, 12)
contagem_regressiva(11, 33)


