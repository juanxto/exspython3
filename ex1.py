nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
media = (nota1+nota2+nota3) / 3
if media >= 6:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')