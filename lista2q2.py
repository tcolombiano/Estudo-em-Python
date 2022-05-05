nota1=float(input('Qual o valor da primeira nota?'))
nota2=float(input('Qual o valor da segunda nota?'))
nota3=float(input('Qual o valor da terceira nota?'))
nota4=float(input('Qual o valor da quarta nota?'))
peso1=1
peso2=2
peso3=3
peso4=4
mediaponderada=((nota1*peso1)+(nota2*peso2)+(nota3*peso3)+(nota4*peso4))/(peso1+peso2+peso3+peso4)
print('O valor da média ponderada dos números digitados é: ',mediaponderada)