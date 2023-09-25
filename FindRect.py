"""
Ввести несколько строк одинаковой длины, состоящих из символов «#» и «.». Ввод заканчивается пустой строкой.
На получившемся поле изображены только прямоугольники, причём они не соприкасаются даже углами.
Вывести количество этих прямоугольников.
"""
GlCounter = 0
Field = []

# Ввод строк до ввода пустой строки
while True:
    line = input()
    if not line:
        break
    Field.append(line)


# Функция для поиска прямоугольников
def find_rectangles(field):
    rectangles = 0
    n = len(field)
    m = len(field[0])

    for i in range(n):
        for j in range(m):
            if field[i][j] == '#':
                rectangles += 1
                # Используем стек для заполнения прямоугольника символами '.'
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if 0 <= x < n and 0 <= y < m and field[x][y] == '#':
                        field[x] = field[x][:y] + '.' + field[x][y + 1:]
                        stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    return rectangles


# Подсчет прямоугольников
GlCounter = find_rectangles(Field)

print(GlCounter)
