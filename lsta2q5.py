'''Calcular a quantidade de litros de combustível gastos em uma viagem,sabendo-se que o carro faz 12km
com 1 litro. Deverão. Ser fornecidos a) tempo gasto na viagem; b) e a velocidade media. 
Apresentar os valores da velocidade media, tempo gasto, distancia percorrida e quatidade de litros gastos.'''
tempo_hora = int(input('Digite a quantidade de tempo gasto em horas'))
tempo_minuto = int(input('Digite a quantidade de tempo gasto em minutos'))
tempo_segundo = int(input('Digite a quantidade de tempo gasto em segudos'))
tempoconvertido = (tempo_hora*3600)+(tempo_minuto*60)
velocidade_media = int(input('Digite a velocidade média '))
espaco = velocidade_media%tempoconvertido
litrogasto = espaco%12
print('O valor da velocidade média em é: ', velocidade_media, 'm/s')
print('O espaço percorrido em metros foi: ', espaco)
print('A quantidade de litros gastos na viagem foi de ', litrogasto, 'L')
