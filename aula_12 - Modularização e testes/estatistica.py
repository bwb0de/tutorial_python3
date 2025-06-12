def calcular_media_aritmetica(lista_numeros, precisao):
    soma = 0
    ne = 0
    for n in lista_numeros:
        soma += n
        ne += 1
    media_aritmetica = soma / ne
    if precisao:
        media_aritmetica = round(media_aritmetica, precisao)
    return media_aritmetica


def identificar_moda(lista_numeros):
    contagem = {}
    for n in lista_numeros:
        if contagem.get(n) is None:
            contagem[n] = 1
        else:
            contagem[n] += 1

    maior_contagem = max(contagem.values())
    resposta = []
    for n, qtd in contagem.items():
        if qtd == maior_contagem:
            resposta.append(n)

    resposta.sort()
    return resposta


    
def calcular_mediana(lista_numeros):
    l = lista_numeros[:]
    l.sort()
    if len(l) % 2 == 0:
        i1 = (len(l)//2) - 1
        i2 = (len(l)//2) 
        return (l[i1] + l[i2]) / 2
    else:
        i = len(l)//2
        return l[i]



def calcular_desvios(lista_numeros, precisao):
    ma = calcular_media_aritmetica(lista_numeros, precisao)
    desvios = []
    for n in lista_numeros:
        desvio = n - ma
        if precisao:
            desvio = round(desvio, precisao)
        desvios.append(desvio)
    desvios.sort()
    return desvios


    
def calcular_variancia(lista_numeros, precisao):
    d = calcular_desvios(lista_numeros, precisao)
    quadrado_dos_desvios = []
    ne = 0
    for n in d:
        ne += 1
        quadrado_dos_desvios.append(n**2)

    variancia = sum(quadrado_dos_desvios) / (ne - 1)
    if precisao:
        variancia = round(variancia, precisao)

    return variancia

    
def calcular_desvio_padrao(lista_numeros, precisao):
    variancia = calcular_variancia(lista_numeros, precisao)
    denominador = len(lista_numeros)

    resposta = variancia ** 0.5
    if precisao:
        resposta = round(resposta, precisao)
    
    return resposta

