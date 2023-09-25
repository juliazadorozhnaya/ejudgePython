"""
Вводится кортеж пар натуральных чисел. Это координаты отрезков на прямой. Рассмотрим объединение этих отрезков
и найдём длину этого объединения (т. е. совокупную длину всех «закрашенных» нашими отрезками отрезков на прямой).
"""

def UniInterval():
    m = eval(input())
    res = []
    for i in m:
        res.append(i)

    res.sort(key=lambda x: x[0])
    begin_seq = res[0][0]
    end_seq = res[0][1]

    l = 0
    for i in res:
        if i[0] <= end_seq <= i[1]:
            begin_seq = min(begin_seq, i[0])
            end_seq = i[1]
        elif end_seq < i[0]:
            l = l + end_seq - begin_seq
            begin_seq = i[0]
            end_seq = i[1]
    l = l + end_seq - begin_seq
    return l

print(UniInterval())