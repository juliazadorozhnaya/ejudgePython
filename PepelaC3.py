def create_subsystems():
    subsystems = ""
    string = input().split()
    while True:
        if len(string[0]) != 1:
            break
        subsystem = f"class {string[0]}"
        if 1 < len(string) and string[1].isupper():
            subsystem += f"({','.join(string[1])})"
        subsystem = f"{subsystem}:\n"
        if 1 < len(string) and string[-1].islower():
            subsystem = f"{subsystem}    {','.join(string[-1])} = {','.join('None' for i in string[-1])}\n"
        else:
            subsystem = f"{subsystem}    pass\n"
        subsystems = f'{subsystems}{subsystem}'
        string = input().split()
    return subsystems, string


def create_pepelac(string):
    pepelac = f"class Pepelac({','.join(string[0])}):\n"
    if len(string) == 3:
        pepelac += f"    {','.join(string[1])} = {','.join('None' for i in string[1])}\n"
    else:
        pepelac += "    pass\n"
    return pepelac


def create_instances(string):
    return ''.join(f"check_pepelac = Pepelac.{i}\n" for i in (string[-1]))


if __name__ == '__main__':
    subsystems, string = create_subsystems()
    code = f'{subsystems}'
    code = f'{code}{create_pepelac(string)}'
    code = f'{code}{create_instances(string)}'
    try:
        exec(code)
    except Exception as e:
        print("Incorrect")
    else:
        print("Correct")
