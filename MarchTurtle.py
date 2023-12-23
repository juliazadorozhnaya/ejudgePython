"""
С помощью конструкции match / case (и только её, условные операторы и иные конструкции с if в этой задачи не разрешены) написать п
рограмму, которая в цикле вводит и интерпретирует перечисленные ниже команды перемещения «черепашки» по координатной
плоскости. Конец ввода — пустая строка. Изначально черепашка находится в точке 0, 0. Все «слова» в команде разделены ровно
одним пробелом. move направление, где направление — это s, n, w или е: переместить черепашку на один шаг вниз, вверх,
влево или вправо соответственно. move: переместить черепашку в том же направлении, указанном последней командой вида move
 направление. Если такой команды ещё не было, черепашка не перемещается. Все остальные команды вида move что-то там должны
 выводить текст Cannot move to что-то там, и не перемещать черепашку retreat: переместить черепашку в направлении, обратном
 последней команде вида move направление. Если такой команды ещё не было, черепашка не перемещается. info что, где что —
 это x , y или xy: вывести абсциссу, ординату или пару «абсцисса ордината» say какое-то сообщение вывести
«какое-то сообщение» (включая пустое) все остальные команды игнорируются Перед выходом из программы дополнительно выполняется команда info xy.
"""

def turtle_interpreter():
    last_move = None
    x, y = 0, 0

    while True:
        command = input().strip()
        if command == "":
            break

        match command.split():
            case ["move", direction] if direction in ["s", "n", "w", "e"]:
                last_move = direction
                if direction == "s":
                    y -= 1
                elif direction == "n":
                    y += 1
                elif direction == "w":
                    x -= 1
                elif direction == "e":
                    x += 1
            case ["move"]:
                if last_move:
                    match last_move:
                        case "s": y -= 1
                        case "n": y += 1
                        case "w": x -= 1
                        case "e": x += 1
            case ["move", unknown_direction]:
                print(f"Cannot move to {unknown_direction}")
            case ["retreat"]:
                if last_move:
                    match last_move:
                        case "s": y += 1
                        case "n": y -= 1
                        case "w": x += 1
                        case "e": x -= 1
            case ["info", "x"]:
                print(x)
            case ["info", "y"]:
                print(y)
            case ["info", "xy"]:
                print(x, y)
            case ["say", *message]:
                print(" ".join(message))
            case _:
                pass

    print(x, y)

turtle_interpreter()
