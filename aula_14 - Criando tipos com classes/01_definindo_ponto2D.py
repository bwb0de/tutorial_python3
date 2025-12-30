#
# Implemente uma classe Ponto2D que possui como atributos "x" e "y", e o
# método "distancia" que recebe outro Ponto2D e retorna a distancia 
# entre eles. 
#
# Implemente os seguintes métodos mágicos (dunder):
#
#   __str__(self) => forma de apresentação quando enviado à função print()
#   __len__(self) => como distância da origem quando enviado à função len()
#   __add__(self, other) [+]
#   __eq__(self, other)  [==]
#   __ne__(self, other)  [!=]
#   __lt__(self, other)  [<]
#   __gt__(self, other)  [>]
#   __le__(self, other)  [<=]
#   __ge__(self, other)  [>=]
#


class Ponto2D:
    def __init__(self, x, y): 
        self.__x = float(x); self.__y = float(y)

    def __str__(self): 
        return f"P[x: {self.__x}; y: {self.__y}]"

    def __len__(self):
        return self.distancia(Ponto2D(0,0))

    def __add__(self, other):
        if not isinstance(other, Ponto2D):
            raise TypeError("Esta operação só é permitida entre instancias Ponto2D...")
        return Ponto2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if not isinstance(other, Ponto2D):
            raise TypeError("Esta operação só é permitida entre instancias Ponto2D...")
        return all([self.x == other.x, self.y == other.y])

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Ponto2D):
            raise TypeError("Esta operação só é permitida entre instancias Ponto2D...")
        return self.__len__() < len(other)
    
    def __gt__(self, other):
        if not isinstance(other, Ponto2D):
            raise TypeError("Esta operação só é permitida entre instancias Ponto2D...")
        return self.__len__() > len(other)

    def __le__(self, other):
        if not isinstance(other, Ponto2D):
            raise TypeError("Esta operação só é permitida entre instancias Ponto2D...")
        return self.__len__() <= len(other)

    def __ge__(self, other):
        if not isinstance(other, Ponto2D):
            raise TypeError("Esta operação só é permitida entre instancias Ponto2D...")
        return self.__len__() >= len(other)

    @property
    def x(self): 
        return self.__x

    @property
    def y(self):
        return self.__y

    def distancia(self, other):
        assert(isinstance(other, Ponto2D))
        dx = other.x - self.x; dy = other.y - self.y 
        return (dx**2 + dy**2) ** 0.5
    


# Testando...
if __name__ == '__main__':
    p1 = Ponto2D(0,0)
    p2 = Ponto2D(3,4)

    print(p1.distancia(p2))
    print(p1, p2)


