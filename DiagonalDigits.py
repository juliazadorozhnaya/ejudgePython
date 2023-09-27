"""Ввести целые M и N, вывести последовательность 0 1 2 3 4 5 6 7 8 9 0 1 2 3 … в виде прямоугольной
матрицы N×M, заполненной из верхнего левого угла по следующему правилу: На каждом шаге заполняется очередная диагональ матрицы
с одинаковой суммой координат Диагонали заполняются поочерёдно сверху вниз и снизу вверх
(таким образом формируется непрерывный «путь» из верхнего левого угла в правый нижний)"""

def fill_matrix(N, M):
    matrix = [[0] * M for _ in range(N)]
    current_value = 0

    for x in range(N + M - 1):
        if x % 2 == 0:
            for i in range(N):
                j = x - i
                if 0 <= j < M:
                    matrix[i][j] = current_value
                    current_value = (current_value + 1) % 10
        else:
            for j in range(M):
                i = x - j
                if 0 <= i < N:
                    matrix[i][j] = current_value
                    current_value = (current_value + 1) % 10

    return matrix

M, N = eval(input())

result_matrix = fill_matrix(N, M)
for row in result_matrix:
    print(" ".join(map(str, row)))
