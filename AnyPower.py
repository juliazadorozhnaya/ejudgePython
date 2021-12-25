import math


def check(n):
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        c = int(i ** int(math.log(n, i)))
        if c == n:
            return 'YES'
    return 'NO'


print(check(int(input())))Ы