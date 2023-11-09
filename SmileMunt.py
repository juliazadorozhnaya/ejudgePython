class Smile:
    def __init__(self, size):
        self.size = size

    def __abs__(self):
        return abs(self.size)

    def __neg__(self):
        return Smile(-self.size)

    def __add__(self, other):
        return Smile(self.size + other.size)

    def __sub__(self, other):
        return Smile(self.size - other.size)

    def __mul__(self, scalar):
        return Smile(self.size * scalar)

    def __str__(self):
        if self.size < 0:
            return "\n/{}-\n| |\n\\/"
        elif self.size == 0:
            return ""
        else:
            eye_distance = self.size // 4
            mouth_distance = self.size // 4
            eye_mouth_distance = self.size // 2
            smile = f"/{self.size}{'-' * (self.size - 2)}\\\n"
            for i in range(1, self.size - 1):
                if i == eye_distance:
                    smile += "|"
                else:
                    smile += " "
                smile += " " * (self.size - 2)
                if i == eye_mouth_distance:
                    smile += "O   O"
                else:
                    smile += " " * 5
                if i == mouth_distance:
                    smile += "|"
                smile += "\n"
            smile += "\\"
            smile += "-" * (self.size - 2)
            smile += "/\n"
            return smile

