class Triangle:
    a = 0
    b = 0
    c = 0
    emp = 0

    def __init__(self, *arg):
        self.a = arg[0]
        self.b = arg[1]
        self.c = arg[2]

        if ((self.a <= 0) or (self.b <= 0) or (self.c <= 0) or (self.a + self.b < self.c) or (
                self.a + self.c < self.b) or (self.c + self.b < self.a)):
            self.emp = 1

    def __abs__(self):
        p = (self.a + self.b + self.c) / 2

        if self.emp == 1:
            return 0
        else:
            return (p * (p - self.a) * (p - self.b) * (p - self.c))**(1/2)

    def __eq__(self, obj):
        if ((self.a == obj.a) or (self.a == obj.b) or (self.a == obj.c)) or ((self.b == obj.a) or (self.b == obj.b) or (self.b == obj.c)) or ((self.c == obj.a) or (self.c == obj.b) or (self.c == obj.c)):
            return True
            #if (self.b == obj.a) or (self.b == obj.b) or (self.b == obj.c):
               # if (self.c == obj.a) or (self.c == obj.b) or (self.c == obj.c):
                    #return True
        return False

    def __ne__(self, obj):
        if self.__abs__() == obj.__abs__():
            return False
        return True

    def __bool__(self):
        if self.emp == 0:
            return True
        return False

    def __lt__(self, obj):
        if self.__abs__() < obj.__abs__():
            return True
        return False

    def __gt__(self, obj):
        if self.__abs__() > obj.__abs__():
            return True
        return False

    def __le__(self, obj):
        if self.__abs__() <= obj.__abs__():
            return True
        return False

    def __ge__(self, obj):
        if self.__abs__() >= obj.__abs__():
            return True
        return False

    def __str__(self):
        s = ""
        s += "{:.1f}".format(self.a)
        s += ":{:.1f}".format(self.b)
        s += ":{:.1f}".format(self.c)
        return s
