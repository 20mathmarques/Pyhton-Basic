idade = int(input('Digite sua idade:'))

carteira = 18
pode_carteira = idade - carteira
falta_cartera = carteira-idade

if idade >=18:
    print('Voce ja pode tirar habilitacao', "\n" ,"Voce tem direito a habilitação ha", pode_carteira, 'ano(s)' )
else:
    print('Voce nao pode tirar habilitacao', "\n" ,"Voce tera direito a habilitação ha", falta_cartera ,'ano(s)' )
