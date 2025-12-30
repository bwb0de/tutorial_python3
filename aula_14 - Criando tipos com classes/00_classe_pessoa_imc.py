#
# Retorne ao código anterior do IMC
#
# Implemente uma classe Pessoa. Esta classe será o modelo para os objetos pessoas
# Que serão criados na medida em que o o arquivo "pessoas.txt" for processado.
#
# A classe Pessoa deverá ter os atributos mínimos: nome, altura e peso.
#
# A classe Pessoa deverá ter o método 'imc', que retorna o valor do IMC,
# e o método 'classificacao_imc' que retorna a situação a partir de um 
# determinado valor do IMC.
#

class Pessoa:
    def __init__(self, nome:str, altura:float, peso:float):
        self.__nome = nome.strip()
        self.__altura = altura
        self.__peso = peso

    def imc(self):
        return round(self.__peso / (self.__altura ** 2),2)

    def classificacao_imc(self):
        imc = self.imc()
        if imc < 17.00: 
            return "Muito abaixo do peso"
        elif 17.00 <= imc <= 18.49: 
            return "Abaixo do peso"
        elif 18.50 <= imc <= 24.99: 
            return "Peso normal"
        elif 25.00 <= imc <= 29.99: 
            return "Acima do peso"
        elif 30.00 <= imc <= 34.99: 
            return "Obesidade I"
        elif 35.00 <= imc <= 39.99: 
            return "Obesidade II (severa)"
        elif imc >= 40.00: 
            return "Obesidade III (mórbida)"

    @property
    def nome(self):
        return self.__nome

    @property
    def altura(self):
        return self.__altura

    @property
    def peso(self):
        return self.__peso


arquivo = open('pessoas.txt')
conteudo = arquivo.read().strip().split("; ")
conteudo = [linha.split(', ') for linha in conteudo]
conteudo = [Pessoa(nome, float(altura), float(peso)) for nome, altura, peso in conteudo]

for pessoa in conteudo:
    print(pessoa.nome.ljust(15), str(pessoa.imc()).ljust(8), pessoa.classificacao_imc())






