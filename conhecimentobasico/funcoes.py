# def , faz com que definamos uma função

#calculadora

def soma(x,y):
    print(x + y)

def sub(x,y):
    print(x - y)

def multi(x,y):
    print(x * y)

def div(x,y):
    print(x / y)
    print('resto', x % y)


operacao = int(input('Digite a operação, se for 1 a operação será soma' '\n'', se for 2 será subtração,'  '\n' ' se for 3 sera multiplicacao,' '\n' 'se for 4 sera divisao: '))
n1 = int(input('Digite o seu primeiro numero: '))
n2 = int(input('Digite o seu segundo numero: '))

if operacao == 1 :
    soma(n1,n2)
elif operacao == 2:
    sub(n1,n2)
elif operacao == 3:
    multi(n1,n2)
elif operacao == 4:
    div(n1,n2)
