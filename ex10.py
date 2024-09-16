salario = float(input('Qual o seu salario: R$'))
totalv = float(input('Qual foi o total das vendas: R$'))
if totalv > 1500:
    totalvv = totalv - 1500
    totalv -= totalvv
    salariototal = ((3 * totalv)/100) + ((5 * totalvv)/100) + salario
    print(f'O salario total é {salariototal}')
else:
    salariototal = ((3 * totalv) / 100)  + salario
    print(f'O salario total é {salariototal}')
