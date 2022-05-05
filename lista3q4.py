'''4. Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!
Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista.
Agora «vá à sorveteria» e se empanturre de sorvete e tire o sorvete da lista.'''

compras_do_mes=['arroz,','feijão','josefina','Biscoito de maisena','placa de ovos','Miojo sabor Yakisoba','Sal','Sorvete','K-Boa','Detergente de pia','Sabonete']
print('A lista do mês é:',compras_do_mes)
#Minha namorada MANDOU eu tirar os produtos de limpeza da lista
del compras_do_mes[8:11]
print('Lista atualizada:',compras_do_mes)
#Eu não gosto de sorvete, vou tirar da lista!
del compras_do_mes[7]
print('A lista atual é :',compras_do_mes)
