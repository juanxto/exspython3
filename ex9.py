tri1 = float(input('Insira o primeiro lado do triangulo: '))
tri2 = float(input('Insira o segundo lado do triângulo: '))
tri3 = float(input('Insira o terceiro lado do triângulo: '))

if tri1 == tri2 == tri3:
    print('Este é um triangulo equilatero')
elif tri1 != tri2 != tri3:
    print('Este é um triangulo escaleno')
else:
    print('Este é um triangulo isosceles')