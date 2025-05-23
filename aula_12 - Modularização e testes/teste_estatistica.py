from estatistica import moda, mediana, media_aritmetica, desvios, variancia, desvio_padrao


def test_moda():
	print("Testando função moda() ", end="")
	assert(moda([2,3,7,4,9,8,1,4,6,5,3,4]) == 4)
	print("=> Ok!")
	

def test_media_aritmetica():
	print("Testando função media_aritmetica() ", end="")
	assert(media_aritmetica([2,3,7,4,9,8,1,4,6,5,3,4], 2) == 4.67)
	assert(media_aritmetica([2,3,7,4,9,8,1,4,6,5,3,4], 3) == 4.667)
	assert(media_aritmetica([2,3,7,4,9,8,1,4,6,5,3,4], 4) == 4.6667)
	assert(media_aritmetica([2,3,7,4,9,8,1,4,6,5,3,4], False) == 4.666666666666667)
	print("=> Ok!")

	
def test_mediana():
	print("Testando função mediana() ", end="")
	assert(mediana([2,3,7,4,9,8,1,4,6,5,3,4]) == 4)
	print("=> Ok!")
	
	
def test_desvios():
	print("Testando função desvios() ", end="")
	assert(desvios([2,3,7,4,9,8,1,4,6,5,3,4], 2) == [-3.67, -2.67, -1.67, -1.67, -0.67, -0.67, -0.67, 0.33, 1.33, 2.33, 3.33, 4.33])
	assert(desvios([2,3,7,4,9,8,1,4,6,5,3,4], 3) == [-3.667, -2.667, -1.667, -1.667, -0.667, -0.667, -0.667,  0.333, 1.333,  2.333,  3.333,  4.333])
	assert(desvios([2,3,7,4,9,8,1,4,6,5,3,4], 4) == [-3.6667, -2.6667, -1.6667, -1.6667, -0.6667, -0.6667, -0.6667, 0.3333,  1.3333,  2.3333,  3.3333,  4.3333])
	assert(desvios([2,3,7,4,9,8,1,4,6,5,3,4], False) == [-3.666666666666667, -2.666666666666667, -1.666666666666667, -1.666666666666667, -0.666666666666667, -0.666666666666667, -0.666666666666667, 0.33333333333333304, 1.333333333333333, 2.333333333333333, 3.333333333333333, 4.333333333333333])
	print("=> Ok!")


def test_variancia():
	print("Testando função variancia() ", end="")
	assert(variancia([2,3,7,4,9,8,1,4,6,5,3,4], 2) == 5.88)	
	assert(variancia([2,3,7,4,9,8,1,4,6,5,3,4], 3) == 5.879)	
	assert(variancia([2,3,7,4,9,8,1,4,6,5,3,4], 4) == 5.8788)	
	assert(variancia([2,3,7,4,9,8,1,4,6,5,3,4], False) == 5.878787878787879)	
	print("=> Ok!")


def test_desvio_padrao():
	print("Testando função desvio_padrao() ", end="")
	assert(desvio_padrao([2,3,7,4,9,8,1,4,6,5,3,4], 2) == 2.42)
	assert(desvio_padrao([2,3,7,4,9,8,1,4,6,5,3,4], 3) == 2.425)
	assert(desvio_padrao([2,3,7,4,9,8,1,4,6,5,3,4], 4) == 2.4246)
	assert(desvio_padrao([2,3,7,4,9,8,1,4,6,5,3,4], False) == 2.424621182533032)
	print("=> Ok!")



if __name__ == '__main__':
	test_moda()
	test_mediana()
	test_media_aritmetica()
	test_desvios()
	test_variancia()
	test_desvio_padrao()
