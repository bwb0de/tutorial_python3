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

print("Jogo: pedra, papel e tesoura")
print("Selecione um número conforme a opção desejada:")
print("1: Pedra")
print("2: Papel")
print("3: Tesoura")
opcao_do_jogador = possibilidades[int(input('[1-3]: '))-1]

print(f"A opção do computador foi {opcao_do_computador}...")

#Testes
empate = opcao_do_jogador == opcao_do_computador
teste_vitoria1 = opcao_do_jogador == 'Pedra' and opcao_do_computador == 'Tesoura'
teste_vitoria2 = opcao_do_jogador == 'Papel' and opcao_do_computador == 'Pedra'
teste_vitoria3 = opcao_do_jogador == 'Tesoura' and opcao_do_computador == 'Papel'
vitoria = teste_vitoria1 or teste_vitoria2 or teste_vitoria3

if empate:
    print("Jogo empatado!")
elif vitoria:
    print("Parabéns! Você venceu!")
else:
    print("Você perdeu... Tente novamente!")


