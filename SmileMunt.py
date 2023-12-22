class Smile:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        if self.size == 0:
            return ""

        abs_size = abs(self.size)
        width = abs_size * 2 + 3
        height = abs_size + 3
        eye_pos = abs_size // 4
        mouth_pos = abs_size // 2

        smiley = [[" " for _ in range(width)] for _ in range(height)]

        # Set borders and corners
        for i in range(width):
            smiley[0][i] = smiley[-1][i] = "-"
        for i in range(height):
            smiley[i][0] = smiley[i][-1] = "|"
        smiley[0][0] = smiley[-1][-1] = "/"
        smiley[0][-1] = smiley[-1][0] = "\\"

        # Set eyes and mouth
        if abs_size > 0:
            smiley[eye_pos + 1][eye_pos + 2] = smiley[eye_pos + 1][-eye_pos - 3] = "O"
            for i in range(eye_pos + 2, width - eye_pos - 2):
                smiley[mouth_pos + 1][i] = "-"

        # Insert size at the top left
        size_str = str(abs(self.size))  # Use absolute value for size
        for i, char in enumerate(size_str):
            smiley[0][i + 1] = char

        # Flip if size is negative
        if self.size < 0:
            smiley = smiley[::-1]
            # Move size to the bottom left
            for i, char in enumerate(size_str):
                smiley[-1][i + 1] = char

        return "\n".join("".join(row) for row in smiley)

    def __neg__(self):
        return Smile(-self.size)

    def __abs__(self):
        return abs(self.size)

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