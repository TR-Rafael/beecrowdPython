import sys


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    idx = 5
    while idx * idx <= num:
        if num % idx == 0 or num % (idx + 2) == 0:
            return False
        idx += 6
    return True


for line in sys.stdin:
    M = []
    for i in range(int(line)):
        M.append(int(input()))
    N = int(input())
    M.reverse()
    total = sum(M[i] for i in range(0, len(M), N))
    conditional = is_prime(total)
    if conditional:
        print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
    else:
        print('Bad boy! I’ll hit you.')
