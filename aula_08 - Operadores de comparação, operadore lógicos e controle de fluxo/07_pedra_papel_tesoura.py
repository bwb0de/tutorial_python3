#
# Complete o código para criar um jogo de pedra-papel-tesoura
#
# O programa deve apresentar uma lista para o usuario de forma que ele selecine
# um numero de 1-3. Cada numero corresponde a uma opção dentre as três possíveis.
#
# O resultado obtido deverá ser comprado com o que foi selecionado pelo computador.
# O programa deverá informar a escolha feita pelo usuário, pelo computador e quem
# foi o vencedor a partir das escolhas feitas.
#

import random

possibilidades = ['Pedra', 'Papel', 'Tesoura']

opcao_do_computador = possibilidades[random.randint(1,3)-1]

