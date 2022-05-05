'''Crie três listas, uma lista de cada coisa a seguir:
• frutas
• docinhos de festa (não se esqueça de brigadeiros!!)
• ingredientes de feijoada
Lembre-se de salvá-las em alguma variável!

a. Agora crie uma lista que contém essas três listas.

b. você consegue acessar o elemento brigadeiro?


c. Adicione mais brigadeiros à segunda lista de listona. O que aconteceu com a lista de docinhos
de festa?

d. Adicione bebidas ao final da listona, mas sem criar uma lista!'''

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
