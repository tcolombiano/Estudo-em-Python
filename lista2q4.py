'''Calcular o salario liquido de um professor. Os dados fornecidos serão: a) valor hora aula; b) numero de
aulas dadas; c) percentual de desconto INSS.'''
valor_hora = float(input('Digite o valor da hora aula: '))
aulas_dadas = float(input('Digite o número de aulas dadas no mês: '))
desconto_inss=float(input('Digite o número de aulas dadas no mês:'))
'''De acordo com o google: 7,5% para quem ganha um salário mínimo (R$ 1.212)'''
total_salario = valor_hora*aulas_dadas
total_salario=total_salario-desconto_inss
print('A bolada do mês é R$', total_salario)
