input_of_problem = input()
a, b, c, d = map(int, input_of_problem.split())

conditional = (b > c) and (d > a) and ((c + d) > (a + b)) and (c > 0) and (d > 0) and (a % 2 == 0)

if conditional:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
