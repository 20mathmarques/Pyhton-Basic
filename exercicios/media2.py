Nota1 = float(input())
Nota2 = float(input())
Nota3 = float(input())

Media = ( (Nota1 + Nota2 + Nota3 ) / 3)
Media = round(Media, 2)
Media_formatada = "{:.2f}".format(Media)

if Media >= 70 and Media <=100:
    print('A media do aluno foi ', '%.2f' % Media_formatada ,' e ele foi APROVADO')
elif Media >=0 and Media <=40 :
    print('A media do aluno foi ', '%.2f' % Media_formatada ,' e ele foi REPROVADO')
else :
    print('A media do aluno foi ', '%.2f' % Media_formatada ,' e ele foi FINAL')   