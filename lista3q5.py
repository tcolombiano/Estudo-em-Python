'''5. Dado uma lista de números, faça com que os números sejam ordenados e, em seguida, inverta a
ordem da lista
usando slicing.'''
lista_numeros = [2, 5, 3, 4, 1, 6, 7, 8, 9, 10]
print('A lista bagunçada é:', lista_numeros)
lista_numeros.sort()
print('A lista atual é ordenada é:', lista_numeros)
lista_invertida = lista_numeros[::-1]
print('A lista invertida é ', lista_invertida)
