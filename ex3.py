
num = int(input('Digite um numero: '))
numdoub = num * 2
if num >= 0:
    print(f'Este é o seu numero {num} e ele é positivo')
else:
    numpos = num - numdoub
    print(f'O numero inserido era negativo, foi transformado no seu equivalente positivo: {numpos}')