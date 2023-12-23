class Smile:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        if self.size == 0:
            return ""

        abs_size = abs(self.size)
        width = abs_size * 2 + 1
        eye_row = abs_size // 4
        mouth_row = 3 * abs_size // 4
        smile_string = ""

        # First line with size
        smile_string += "/" + str(abs_size) + "-" * (width - 4) + "\\\n"

        # Upper empty part
        for i in range(eye_row - 1):
            smile_string += "|" + " " * (width - 2) + "|\n"

        # Eyes
        eye_pos = abs_size // 4
        if self.size > 0:
            smile_string += "|" + " " * eye_pos + "O" + " " * (width - 2 * eye_pos - 2) + "O" + " " * eye_pos + "|\n"
        else:
            smile_string += "|" + " " * eye_pos + "0" + " " * (width - 2 * eye_pos - 2) + "0" + " " * eye_pos + "|\n"

        # Middle empty part
        for i in range(mouth_row - eye_row - 1):
            smile_string += "|" + " " * (width - 2) + "|\n"

        # Mouth
        smile_string += "|" + " " * (eye_pos + 1) + "-" * (width - 2 * (eye_pos + 1) - 2) + " " * (eye_pos + 1) + "|\n"

        # Bottom empty part
        for i in range(abs_size - mouth_row - 1):
            smile_string += "|" + " " * (width - 2) + "|\n"

        # Last line
        smile_string += "\\" + "-" * (width - 2) + "/"

        return smile_string

    def __abs__(self):
        return abs(self.size)

    def __neg__(self):
        return Smile(-self.size)

    def __add__(self, other):
        return Smile(self.size + other.size)

    def __sub__(self, other):
        return Smile(self.size - other.size)

    def __mul__(self, number):
        return Smile(self.size * number)

print(abs(Smile(-2)))
print(Smile(1))
print(Smile(1) - Smile(4))
print(-Smile(2) + Smile(-2))
print(Smile(6) * 3 - Smile(1))