import unittest
from field import Field, Element
class TestField(unittest.TestCase):

    def test_addition(self):
        x = Element(1, 1, 2)
        y = Element(2, 0, 2)
        f = Field(3) # Z_3
        # in Z_3, x + y = (0, 1, 1)
        z = f.addition(x, y)
        assert z.a == 0
        assert z.b == 1
        assert z.c == 1

if __name__ == '__main__':
    unittest.main()