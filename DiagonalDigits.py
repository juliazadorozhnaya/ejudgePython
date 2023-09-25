"""Ввести целые M и N, вывести последовательность 0 1 2 3 4 5 6 7 8 9 0 1 2 3 … в виде прямоугольной
матрицы N×M, заполненной из верхнего левого угла по следующему правилу: На каждом шаге заполняется очередная диагональ матрицы
с одинаковой суммой координат Диагонали заполняются поочерёдно сверху вниз и снизу вверх
(таким образом формируется непрерывный «путь» из верхнего левого угла в правый нижний)"""

def fill_matrix(M, N):
    matrix = [[0] * M for _ in range(N)]  # Создаем матрицу NxM, заполненную нулями
    current_value = 0  # Начальное значение для заполнения диагоналей

    # Заполняем матрицу по диагоналям
    for diagonal_sum in range(M + N - 1):
        if diagonal_sum < M:
            row, col = 0, diagonal_sum
        else:
            row, col = diagonal_sum - M + 1, M - 1

        while row < N and col >= 0:
            matrix[row][col] = current_value
            current_value = (current_value + 1) % 10  # Зацикливаем значения от 0 до 9
            row += 1
            col -= 1

    return matrix

# Ввод размеров матрицы
M, N = eval(input())

# Заполняем матрицу и выводим ее
result_matrix = fill_matrix(M, N)
for row in result_matrix:
    print(" ".join(map(str, row)))