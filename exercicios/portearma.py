Nacionalidade = input('Digite sua nacionalidade: ')
Ocupacao = input('Digite sua ocupação: ')
Qtd_Arma = int(input('Digite a qtd de armas portadas: '))
Calibre = int(input('Digite o calibre da arma: '))

if Nacionalidade == 'E' and Qtd_Arma < 1 :
    print('Liberado')
    print(type(Qtd_Arma))

elif Nacionalidade == 'B' and Ocupacao == 'M':
    print('Liberado')
    print(type(Ocupacao))

elif Nacionalidade =='B' and Ocupacao == 'T' or 'O' and Qtd_Arma <= 1 and Calibre <= 22:
    print(type(Ocupacao))
    print('Liberado')
elif Nacionalidade =='B' and Ocupacao == 'C' and Qtd_Arma <=2 and Calibre <=38:
    print('Liberado')
    print(type(Ocupacao))

else:
    print('Barrado')