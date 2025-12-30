#
# Crie um programa que leia o tamanho de três segmentos de reta. Indique se a partir
# dos valores recebidos é possível formar um triângulo. Informe, também, qual o tipo
# de triângulo pode ser formado a partir das medidas apresentadas:
#   - equilatero (todos lados iguais)
#   - isosceles (dois lados iguais)
#   - escaleno (todos lados diferentes)
#
# Obs: para que três segmentos possam formar um triângulo, o comprimento de cada lado
# deve ser menor que a soma dos outros dois
#

seg1, seg2, seg3 = input("Informe o valor dos segmentos 1, 2 e 3 separando-os com um espaço:").replace(",",".").strip().split()

seg1, seg2, seg3 = float(seg1), float(seg2), float(seg3)

#Testes
lado1_ok = seg1 < (seg2 + seg3)
lado2_ok = seg2 < (seg1 + seg2)
lado3_ok = seg3 < (seg1 + seg2)
equilatero = seg1 == seg2 and seg2 == seg3
isosceles  = seg1 == seg2 or seg2 == seg3 or seg1 == seg3

if lado1_ok and lado2_ok and lado3_ok:
    if equilatero:
        print("Forma um triângulo equilátero")
    elif isosceles:
        print("Forma um triangulo isósceles")
    else:
        print("Forma um triangulo escaleno")
else:
    print("Não forma triângulo")


