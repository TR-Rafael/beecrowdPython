def greater_than(valueA, valueB):
    return int((valueA + valueB + abs(valueA - valueB)) / 2)


input_of_problem = input()
a, b, c = map(int, input_of_problem.split())

print(f'{greater_than(greater_than(a,b), c)} eh o maior')
