#
# Crie um programa que receba um verbo no infinitivo terminado em 'ar' ou 'er' e retorne sua
# conjugação no presente 
#
# Dica: usar dicionários aninhados com listas e fatiamento
#

flexoes_verbais = {
    'ar': [
        'o',
        'as',
        'a',
        'amos',
        'ais',
        'am'
    ],
    'er': [
        'o',
        'es',
        'e',
        'emos',
        'eis',
        'em'
    ]
}

verbo_infinitivo = input("Informe o verbo no infinitivo: ").strip()
terminacao = verbo_infinitivo[-2:]

print("Presente do indicativo:")

primeira_pessoa = verbo_infinitivo[:-2] + flexoes_verbais[terminacao][0]
primeira_pessoa_init = primeira_pessoa[:-3]
primeira_pessoa_end = primeira_pessoa[-3:].replace('eco', 'eço')
primeira_pessoa = primeira_pessoa_init + primeira_pessoa_end

print(f"Eu {primeira_pessoa}")
print(f"Tu {verbo_infinitivo[:-2]}{flexoes_verbais[terminacao][1]}")
print(f"Ele {verbo_infinitivo[:-2]}{flexoes_verbais[terminacao][2]}")
print(f"Nós {verbo_infinitivo[:-2]}{flexoes_verbais[terminacao][3]}")
print(f"Vós {verbo_infinitivo[:-2]}{flexoes_verbais[terminacao][4]}")
print(f"Eles {verbo_infinitivo[:-2]}{flexoes_verbais[terminacao][5]}")

