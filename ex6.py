horas = int(input('Que horas são: '))
min = int(input('Que minutos são: '))

if horas > 23 or horas < 0 or min < 0 or min > 59:
    print('São validas as horas entre 00:00 e 23:59')
else:
    print(f'Horario atual: {horas}:{min}')