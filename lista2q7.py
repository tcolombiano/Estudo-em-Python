'''Criar um programa que leia a quantidade de fitas de uma locadora de vídeo possui e o valor que ela cobra
por cada aluguel, mostrando as informações pedidas a seguir: a) sabendo que um terço das fitas são
alugadas por mês, exiba o faturamento anual da locadora; b)Quando o cliente atrasa a entrega, é cobrada
uma multa de 10% sobre o valor do aluguel. Sabendo que um decimo das fitas alugadas no mês são
devolvidas com atraso, calcule o valor ganho com multas por mês; c) sabendo ainda que 2% de fitas se
estragam ao longo do ano, e um decimo do total é comprado para reposição, exiba a quantidade de fitas
que a locadora terá no final do ano'''

valor_aluguel_fita = float(input(('Qual o valor do aluguel por fita ?')))
quantidade_total_fitas = int(input('Digite a quantidade de fitas na locadora:'))
quantidade_fitas_locadas = quantidade_total_fitas/3
# a) sabendo que um terço das fitas são alugadas por mês. 1/3 do quantidade_fitas_total ( faturamento anual)
faturamento_anual = quantidade_fitas_locadas*12*valor_aluguel_fita
# b)Quando o cliente atrasa a entrega, é cobrada uma multa de 10% sobre o valor do aluguel. 10%*valor_fita
# Sabendo que um decimo das fitas alugadas no mês são devolvidas com atraso 1/10 fitas_alugadas_mes
quantidade_fitas_multa = quantidade_fitas_locadas/10
multa = (valor_aluguel_fita*0.10)*quantidade_fitas_multa
multa= round(multa,2)
# c)sabendo ainda que 2% de fitas se estragam ao longo do ano 2% do total_fitas
fitas_estragadas=quantidade_total_fitas*0.2
quantidade_fitas_final_ano=quantidade_total_fitas-(fitas_estragadas+(quantidade_total_fitas)/10)
print('O faturamento anual é R$',faturamento_anual)
print('O valor ganho de multas é R$',multa)
print('O total de fitas no final do ano é:',quantidade_fitas_final_ano)