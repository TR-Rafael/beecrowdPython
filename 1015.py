import math

pont1 = input()
pont2 = input()
x1, y1 = map(float, pont1.split())
x2, y2 = map(float, pont2.split())
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f'{distance:.4f}')

