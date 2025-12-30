#
# Crie um programa que recebe a um verbo no infinitivo, terminado em 'ar'
# e imprima as conjugações verbais desse verbo no presente
#
# Dica: utilizar slicing 
#

verbo_infinitivo = input("Informe um verbo no infinitivo com terminação 'ar': ")

print("Presente do indicativo: ")
print(f"Eu {verbo_infinitivo[:-2]}o")
print(f"Tu {verbo_infinitivo[:-2]}as")
print(f"Ele {verbo_infinitivo[:-2]}a")
print(f"Nós {verbo_infinitivo[:-2]}amos")
print(f"Vós {verbo_infinitivo[:-2]}ais")
print(f"Eles {verbo_infinitivo[:-2]}am")

 
