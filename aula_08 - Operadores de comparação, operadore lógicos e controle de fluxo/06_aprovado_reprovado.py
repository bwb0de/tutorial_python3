#
# Faça um programa que receba 3 notas e o número de faltas de um estudante e
# informe sua mensão (da mais alta à mais baixa): SS, MS, MM, MI, II ou SR.
#
# Apresente, também uma mensagem informando se ele foi aprovado ou reprovado.
#
# Use os critérios da UnB para mensão. E considere que o total de aulas no
# curso em questão é 30 em um semestre. Lembre-se que estudantes com 25% ou mais
# de faltas recebem mensão SR, independente das notas obtidas nas avaliações
# 


TOTAL_AULAS = 30

print("Calculando mensão final da disciplina...")

n1 = float(input("1ª nota [0-10]: ").replace(',','.'))
n2 = float(input("2ª nota [0-10]: ").replace(',','.'))
n3 = float(input("3ª nota [0-10]: ").replace(',','.'))
faltas = int(input("Número de faltas: "))

media = round((n1 + n2 + n3) / 3, 2)

# Testes
reprovado_faltas = (faltas / TOTAL_AULAS) > 0.25
mensao_SS = 10.00 > media >= 9.00
mensao_MS = 9.00 > media >= 7.00
mensao_MM = 7.00 > media >= 5.00
mensao_MI = 5.00 > media >= 2.50
mensao_II = 2.50 > media >  0.00
mensao_SR = media == 0.00

if reprovado_faltas:
    print("Estudante reprovado por faltas, mensão SR")
elif mensao_SS:
    print("Estudante aprovado, mensão SS")
elif mensao_MS:
    print("Estudante aprovado, mensão MS")
elif mensao_MM:
    print("Estudante aprovado, mensão MM")
elif mensao_MI:
    print("Estudante reprovado, mensão MI")
elif mensao_II:
    print("Estudante reprovado, mensão II")
elif mensao_SR:
    print("Estudante reprovado, mensão SR")
else:
    print("Caso não previsto, as notas foram fornecidas dentro da escala de 0-10?")

