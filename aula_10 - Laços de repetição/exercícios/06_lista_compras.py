#
# Implemente um programa caixa registrador. A cada iteração é questionado o produto,
# o valor unitário e a quantidade comprada. Deve haver um código ou convenção para
# finalizar o registro das compras. Ao final, apresente o valor total ao usuário na tela
# e salve a lista de protudos, com suas respectivas informações em um arquivo mercado.txt
#

print("Caixa Registradora, digite -1 em 'Produto' para fechar o programa:")

LARGURA_COLUNA_PRODUTOS = 15
LARGURA_COLUNA_QUANTIDADE = 3
LARGURA_COLUNA_PRECO_UNITARIO = 10
LARGURA_COLUNA_CUSTO = 10
LARGURA_TOTAL = LARGURA_COLUNA_PRODUTOS + LARGURA_COLUNA_QUANTIDADE + LARGURA_COLUNA_PRECO_UNITARIO + LARGURA_COLUNA_CUSTO



lista_produtos = []
total = 0.0
primeira_iteracao = True


while True:
    produto = input('Produto: ')
    
    if produto.strip() == '-1':
        lista_produtos.append('-' * LARGURA_TOTAL + '--')

        lista_produtos.append(''.join(
             ('TOTAL CUSTO'.ljust(LARGURA_COLUNA_PRODUTOS),
              ''.center(LARGURA_COLUNA_QUANTIDADE),
              ''.rjust(LARGURA_COLUNA_PRECO_UNITARIO),
              str('R$'+str(total)).rjust(LARGURA_COLUNA_CUSTO+2)
        )))

        break
           
    
    qtd, preco = input("Quantidade: "), input("Preco: ").replace(",",".")
    qtd, preco = int(qtd), float(preco)

    if primeira_iteracao:
        lista_produtos.append(''.join(
            ('PRODUTO'.ljust(15),
             'QTD'.center(5),
             'P.UNIT'.rjust(10),
             'CUSTO'.rjust(10)
        )))

        primeira_iteracao = False

    lista_produtos.append(''.join((
        produto.strip().ljust(15),
        str(qtd).center(5),
        str('R$'+str(preco)).rjust(10),
        str('R$'+str(round(qtd*preco,2))).rjust(10))))

    total += round(qtd*preco,2); print('')


arquivo = open('mercado.txt', 'w')
arquivo.write('\n'.join(lista_produtos)+'\n')
arquivo.close()
print(f'Total: R${total}')


