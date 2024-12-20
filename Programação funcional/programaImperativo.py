def calcular_media_imperativa(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)

numeros = [1, 2, 3, 4, 5]
media = calcular_media_imperativa(numeros)
print(media)