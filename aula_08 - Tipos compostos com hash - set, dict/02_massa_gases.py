#
# Crie um programa que receba 2 inputs, cada um constituído de um número e um símbolo
# representando um dos gases nobres da tabela periódica. O número e o símbolo de cada
# input deve ser separado por um espaço. O programa deverá retornar o valor da massa
# atômica total conforme a quantidade e os tipos de gás indicado.
#
# Dica: usar dicionário para registrar, no código, os valores de massa dos gases nobres.
#
# Massas aproximadas: 
#     He (Hélio)       =>   4.003
#     Ne (Neônio)      =>  20.180
#     Ar (Argônio)     =>  39.948
#     Kr (Criptônio)   =>  83.798
#     Xe (Xenônio)     => 131.293
#     Rn (Radônio)     => 220.000
#     Og (Oganessônio) => 294.000
#


massas_gases_nobres = {
    'He': 4003,
    'Ne': 20180,
    'Ar': 39948,
    'Kr': 83798,
    'Xe': 131293,
    'Rn': 220000,
    'Og': 294000
}

print("Gases cadastrados: He, Ne, Ar, Kr, Xe, Rn, Og...")
n_atomos1, atomo1_t = input("Forneça a quantidade e o tipo do 1º gás nobre: ").strip().split()
n_atomos1, atomo1_t = int(n_atomos1), massas_gases_nobres[atomo1_t]
n_atomos2, atomo2_t = input("Forneça a quantidade e o tipo do 2º gás nobre: ").strip().split()
n_atomos2, atomo2_t = int(n_atomos2), massas_gases_nobres[atomo2_t]

massa_atomica_total = ((n_atomos1 * atomo1_t) + (n_atomos2 * atomo2_t)) / 1000

print(f"A massa atômica total é: {massa_atomica_total}")
