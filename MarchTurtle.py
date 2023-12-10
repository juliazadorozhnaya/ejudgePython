x, y = 0, 0
last_direction = None

while True:
    command = input("")
    if not command:
        break

    match command.split()[0]:
        case "move":
            direction = command.split()[1] if len(command.split()) > 1 else last_direction
            match direction:
                case "n":
                    y += 1
                    last_direction = "n"
                case "s":
                    y -= 1
                    last_direction = "s"
                case "e":
                    x += 1
                    last_direction = "e"
                case "w":
                    x -= 1
                    last_direction = "w"
                case _:
                    print(f"Cannot move to {direction}")
        case "retreat":
            if last_direction:
                match last_direction:
                    case "n":
                        y -= 1
                    case "s":
                        y += 1
                    case "e":
                        x -= 1
                    case "w":
                        x += 1
            else:
                print("Cannot retreat without previous move")
        case "info":
            if len(command.split()) > 1:
                what = command.split()[1]
                match what:
                    case "x":
                        print(x)
                    case "y":
                        print(y)
                    case "xy":
                        print(f"{x} {y}")
            else:
                print("Invalid info command")
        case "say":
            print(' '.join(command[1:]))
        case _:
            if command and command[0] != "jump":
                print(f"Cannot move to {' '.join(command[1:])}")

print(x, y)