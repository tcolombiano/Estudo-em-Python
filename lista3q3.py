'''3 Utilizando o del, remova todos os elementos da lista criada anteriormente até a lista ficar vazia'''

frutas = ['maça', 'uva']
print('A lista de frutas é:', frutas)
doces = ['casadinho', 'bem casado', 'brigadeiros']
print('A lista de doces é:', doces)
ingredientes_feijoada = ['calabresa', 'carne seca', 'tocinho', 'bacon']
print('Os ingredientes da feijoada são:', ingredientes_feijoada)

lista_geral = [frutas, doces, ingredientes_feijoada]
print('A lista atual é:', lista_geral)

lista_geral.insert(3, 'cerveja')
print('A lista atual agora é:', lista_geral)

del lista_geral[:]
print('Agora a lista está vazia',lista_geral)
