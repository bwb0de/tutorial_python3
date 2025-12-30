from estatistica import identificar_moda, calcular_mediana, calcular_media_aritmetica, calcular_desvios, calcular_variancia, calcular_desvio_padrao


def test_moda():
    print("Testando função identificar_moda() ", end="")
    try:
        assert(identificar_moda([2,3,7,4,9,8,1,4,6,5,3,4]) == [4])
        assert(identificar_moda([2,3,7,4,3,8,1,4,6,5,3,4]) == [3,4])
        assert(identificar_moda([3,3,7,4,9,8,9,4,9,5,3,4]) == [3,4,9])
        print("=> Ok!")
    except TypeError:
        print("=> Falhou! A função foi implementada?")
    

def test_media_aritmetica():
    print("Testando função calcular_media_aritmetica() ", end="")
    try:
        assert(calcular_media_aritmetica([2,3,7,4,9,8,1,4,6,5,3,4], 2) == 4.67)
        assert(calcular_media_aritmetica([2,3,7,4,9,8,1,4,6,5,3,4], 3) == 4.667)
        assert(calcular_media_aritmetica([2,3,7,4,9,8,1,4,6,5,3,4], 4) == 4.6667)
        assert(calcular_media_aritmetica([2,3,7,4,9,8,1,4,6,5,3,4], False) == 4.666666666666667)
        print("=> Ok!")
    except TypeError:
        print("=> Falhou! A função foi implementada?")

    
def test_mediana():
    print("Testando função calcular_mediana() ", end="")
    try:
        assert(calcular_mediana([2,3,7,4,9,8,1,4,6,5,3,4]) == 4)
        print("=> Ok!")
    except TypeError:
        print("=> Falhou! A função foi implementada?")
    
    
def test_desvios():
    print("Testando função calcular_desvios() ", end="")
    try:
        assert(calcular_desvios([2,3,7,4,9,8,1,4,6,5,3,4], 2) == [-3.67, -2.67, -1.67, -1.67, -0.67, -0.67, -0.67, 0.33, 1.33, 2.33, 3.33, 4.33])
        assert(calcular_desvios([2,3,7,4,9,8,1,4,6,5,3,4], 3) == [-3.667, -2.667, -1.667, -1.667, -0.667, -0.667, -0.667,  0.333, 1.333,  2.333,  3.333,  4.333])
        assert(calcular_desvios([2,3,7,4,9,8,1,4,6,5,3,4], 4) == [-3.6667, -2.6667, -1.6667, -1.6667, -0.6667, -0.6667, -0.6667, 0.3333,  1.3333,  2.3333,  3.3333,  4.3333])
        assert(calcular_desvios([2,3,7,4,9,8,1,4,6,5,3,4], False) == [-3.666666666666667, -2.666666666666667, -1.666666666666667, -1.666666666666667, -0.666666666666667, -0.666666666666667, -0.666666666666667, 0.33333333333333304, 1.333333333333333, 2.333333333333333, 3.333333333333333, 4.333333333333333])
        print("=> Ok!")
    except TypeError:
        print("=> Falhou! A função foi implementada?")


def test_variancia():
    print("Testando função calcular_variancia() ", end="")
    try:
        assert(calcular_variancia([2,3,7,4,9,8,1,4,6,5,3,4], 2) == 5.88)    
        assert(calcular_variancia([2,3,7,4,9,8,1,4,6,5,3,4], 3) == 5.879)    
        assert(calcular_variancia([2,3,7,4,9,8,1,4,6,5,3,4], 4) == 5.8788)    
        assert(calcular_variancia([2,3,7,4,9,8,1,4,6,5,3,4], False) == 5.878787878787879)    
        print("=> Ok!")
    except TypeError:
        print("=> Falhou! A função foi implementada?")


def test_desvio_padrao():
    print("Testando função calcular_desvio_padrao() ", end="")
    try:
        assert(calcular_desvio_padrao([2,3,7,4,9,8,1,4,6,5,3,4], 2) == 2.42)
        assert(calcular_desvio_padrao([2,3,7,4,9,8,1,4,6,5,3,4], 3) == 2.425)
        assert(calcular_desvio_padrao([2,3,7,4,9,8,1,4,6,5,3,4], 4) == 2.4246)
        assert(calcular_desvio_padrao([2,3,7,4,9,8,1,4,6,5,3,4], False) == 2.424621182533032)
        print("=> Ok!")
    except TypeError:
        print("=> Falhou! A função foi implementada?")



if __name__ == '__main__':
    test_moda()
    test_mediana()
    test_media_aritmetica()
    test_desvios()
    test_variancia()
    test_desvio_padrao()
