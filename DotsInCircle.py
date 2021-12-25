from math import sqrt
from pickle import TRUE

x, y, r = map(int, input().split(','))
n = 0
a = []

while True:
    x_1, y_1 = map(int, input().split(','))
    n += 1

    if x_1 == 0 and y_1 == 0:
        break
    r_1 = sqrt((x_1 - x) ** 2 + (y_1 - y) ** 2)
    a.append(r_1)

flag = True
for i in range(len(a)):
    if a[i] > r:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')