import math

input_of_problem = input()
A, B, C = map(float, input_of_problem.split())
Delta = (B ** 2) - 4 * A * C

if Delta < 0 or A == 0:
    print('Impossivel calcular')
else:
    print(f'R1 = {(- B + math.sqrt(Delta))/(2*A):.5f}')
    print(f'R2 = {(- B + (math.sqrt(Delta) * - 1))/(2*A):.5f}')
