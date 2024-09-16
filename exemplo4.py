nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
faltas = int(input('Quantidade de faltas: '))
media = (nota1 + nota2) / 2

if media >= 6:
    if faltas < 20:
        print('Aprovado')
    else:
        print('Reprovado por falta')
else:
    print('Reprovado por média')