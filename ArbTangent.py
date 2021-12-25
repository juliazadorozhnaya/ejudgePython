from decimal import *

def pi():
    getcontext().prec += 2
    three = Decimal(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s

A = input()
prec = int(input())
getcontext().prec = 2000

A = Decimal(A)
Pi = Decimal(pi())

angle = Pi * A / Decimal(200)

sin_x = Decimal(0) #first
next_el = angle
for i in range(1, 1000, 1):
    sin_x += (-1)**(i+1) * next_el
    next_el *= (angle ** 2) / (2 * i * (2 * i + 1))

cos_x = Decimal(0) #first
next_el = Decimal(1)
for i in range(1000):
    cos_x += (-1)**i * next_el
    next_el *= (angle ** 2) / (2 * (i + 1) * (2 * i + 1))

getcontext().prec = prec
tg_x = sin_x/cos_x
print(tg_x)
