from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        out = '[' + str(self.pt1) + ', ' + str(self.pt2) + ']'
        return out

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        out = 'Rectangle(' + str(self.pt1.x) + ', ' + str(self.pt1.y) + ', ' + str(self.pt2.x) + ', ' + str(self.pt2.y) + ')'
        return out

    def __eq__(self, other):   # obsługa rect1 == rect2
        return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):            # pole powierzchni
        return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)

# Kod testujący moduł.
import unittest

class TestRectangle(unittest.TestCase): 
	def setUp(self):
		self.rect1 = Rectangle(1, 2, 3, 4)
		self.rect2 = Rectangle(3, 4, 0, -2)

	def test_str(self):
		self.assertEqual(self.rect1.__str__(), "[(1, 2), (3, 4)]")	

	def test_repr(self):
		self.assertEqual(self.rect1.__repr__(), "Rectangle(1, 2, 3, 4)")

	def test_eq(self):
		self.assertEqual(self.rect1 == self.rect1, True)
		self.assertEqual(self.rect1 == self.rect2, False)

	def test_center(self):
		self.assertEqual(self.rect1.center(), Point(2, 3))
		self.assertEqual(self.rect2.center(), Point(1.5, 1))

	def test_area(self):
		self.assertEqual(self.rect1.area(), 4)
		self.assertEqual(self.rect2.area(), 18)

	def test_move(self):
		self.rect1.move(2, 1)
		self.rect2.move(2, 1)
		self.assertEqual(self.rect1, Rectangle(3, 3, 5, 5))
		self.assertEqual(self.rect2, Rectangle(5, 5, 2, -1))


if __name__ == '__main__':
	unittest.main()