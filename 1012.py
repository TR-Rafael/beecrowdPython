PI = 3.14159
input_of_problem = input()
A, B, C = map(float, input_of_problem.split())

print(f'TRIANGULO: {(A * C)/2:.3f}')
print(f'CIRCULO: {PI * C ** 2:.3f}')
print(f'TRAPEZIO: {((A + B) * C)/2:.3f}')
print(f'QUADRADO: {B ** 2:.3f}')
print(f'RETANGULO: {A * B:.3f}')
