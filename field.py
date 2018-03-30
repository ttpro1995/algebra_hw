class Field:
    def __init__(self, m):
        """

        :param m: modulo
        """
        self.m = m
        pass

    def addition(self, x, y):
        """

        :param x: element x
        :param y: element y
        :return:
        """

        a = (x.a + y.a) % self.m
        b = (x.b + y.b) % self.m
        c = (x.c + y.c) % self.m
        return Element(a, b, c)


class Element:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

