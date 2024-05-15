rounds = int(input())
import math

def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def circle_range(spell_type, n):
    if spell_type == 'fire':
        if n == 1:
            return 20
        elif n == 2:
            return 30
        elif n == 3:
            return 50
    elif spell_type == 'water':
        if n == 1:
            return 10
        elif n == 2:
            return 25
        elif n == 3:
            return 40
    elif spell_type == 'earth':
        if n == 1:
            return 25
        elif n == 2:
            return 55
        elif n == 3:
            return 70
    elif spell_type == 'air':
        if n == 1:
            return 18
        elif n == 2:
            return 38
        elif n == 3:
            return 60

def circle_intersects_rectangle(x, y, radius, rx, ry, width, height):
    distance_to_rectangle_center = distance_between_points(x, y, rx + width / 2, ry + height / 2)
    if distance_to_rectangle_center <= radius:
        return True  # The circle may be inside the rectangle or intersecting the rectangle
    else:
        # Check if the circle intersects the sides of the rectangle
        distance_x = abs(x - (rx + width / 2))
        distance_y = abs(y - (ry + height / 2))
        if distance_x > (width / 2 + radius) or distance_y > (height / 2 + radius):
            return False  # The circle is outside the rectangle
        elif distance_x <= (width / 2) or distance_y <= (height / 2):
            return True  # The circle intersects the rectangle
        else:
            return (distance_x - width / 2) ** 2 + (distance_y - height / 2) ** 2 <= radius ** 2

for line in range(rounds):
    dimensions_of_round = input()
    w, h, x0, y0 = map(int, dimensions_of_round.split())
    spell_identifier = input()
    type_of_spell = spell_identifier.split()[0]
    N = int(spell_identifier.split()[1])
    cx, cy = map(int, spell_identifier.split()[2:])
    xf = x0 + w
    yf = y0 + h

    xm = x0 - xf
    ym = y0 - yf
    result = circle_intersects_rectangle(cx, cy, circle_range(type_of_spell, N), x0, y0, w, h)

    if result:
        if type_of_spell == 'fire':
            print('200')
        elif type_of_spell == 'water':
            print('300')
        elif type_of_spell == 'earth':
            print('400')
        elif type_of_spell == 'air':
            print('100')
    else:
        print('0')
