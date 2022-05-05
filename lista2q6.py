'''Entrar com valor de um empréstimo, a taxa de juros e a quantidade de meses. Fazer um programa que
calcule o valor da prestação.'''
valor_do_emprestimo = float(input('Qual o valor do empréstimo ?'))
taxa_juros = float(input('Qual o valor da taxa de juros?'))
taxa_juros = taxa_juros/100
meses = int(input('Em quantos meses quer pagar ?'))
coeficiente = (taxa_juros)/ (1 - (1)/(1+taxa_juros)**meses)
valor_prestacao=valor_do_emprestimo*coeficiente
valor_prestacao=round(valor_prestacao,3)
print('O valor da prestação mensal é R$', valor_prestacao,
      '.Veja se vale a pena mesmo pegar esse empréstimo, banco não é amigo de ninguém.')
