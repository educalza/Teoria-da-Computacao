from functools import reduce

def calcular_media_funcional(numeros):
    soma = reduce(lambda x, y: x + y, numeros)
    return soma / len(numeros)

numeros = [1, 2, 3, 4, 5]
media = calcular_media_funcional(numeros)
print(media)