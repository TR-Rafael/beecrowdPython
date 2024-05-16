value = float(input())
output = ''

if 0 <= value <= 25:
    output = '[0,25]'
elif 25 < value <= 50:
    output = '(25,50]'
elif 50 < value <= 75:
    output = '(50,75]'
elif 75 < value <= 100:
    output = '(75,100]'

if output == '':
    print('Fora de intervalo')
else:
    print(f'Intervalo {output}')
