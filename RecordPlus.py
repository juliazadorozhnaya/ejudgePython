x, y = 0, 0
last_direction = None

while True:
    command = input().split()

    if not command:
        break

    match command[0] if command else None:
        case "move" if len(command) == 2 and command[1] in {'s', 'n', 'w', 'e'}:
            direction = command[1]
            last_direction = direction
            match direction:
                case 's':
                    y -= 1
                case 'n':
                    y += 1
                case 'w':
                    x -= 1
                case 'e':
                    x += 1
        case "move":
            match last_direction:
                case 's':
                    y -= 1
                case 'n':
                    y += 1
                case 'w':
                    x -= 1
                case 'e':
                    x += 1
        case "info" if len(command) == 2 and command[1] in {'x', 'y', 'xy'}:
            info_type = command[1]
            match info_type:
                case 'x':
                    print(x)
                case 'y':
                    print(y)
                case 'xy':
                    print(f"{x} {y}")
        case "say":
            print(' '.join(command[1:]))
        case _:
            if command and command[0] != "jump":
                print(f"Cannot move to {' '.join(command[1:])}")

# Выполнение команды info xy перед выходом из программы
print(f"{x} {y}")
