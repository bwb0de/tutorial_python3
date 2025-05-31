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


class Ponto2D:
	def __init__(self, x, y): self.__x = float(x); self.__y = float(y)
	def __str__(self): return f"P[x: {self.__x}; y: {self.__y}]"
	@property
	def x(self): return self.__x
	@property
	def y(self): return self.__y
	def distancia(self, other):
		assert(isinstance(other, Ponto2D))
		dx = other.x - self.x; dy = other.y - self.y 
		return (dx**2 + dy**2) ** 0.5
    
p1 = Ponto2D(0,0)
p2 = Ponto2D(3,4)

print(p1.distancia(p2))
print(p1, p2)
