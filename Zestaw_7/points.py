import math
import unittest

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        out = '(' + str(self.x) + ', ' + str(self.y) + ')'
        return out

    def __repr__(self):        # zwraca string "Point(x, y)"
        out = 'Point(' + str(self.x) + ', ' + str(self.y) + ')'
        return out

    def __eq__(self, other):   # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        x_out = self.x + other.x
        y_out = self.y + other.y
        return Point(x_out, y_out)

    def __sub__(self, other):  # v1 - v2
        x_out = self.x - other.x
        y_out = self.y - other.y
        return Point(x_out, y_out)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(self.x**2 + self.y**2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.
class TestPoint(unittest.TestCase): 
	def setUp(self):
		self.p1=Point(1, 1)
		self.p2=Point(1, 0)
		self.p3=Point(3, 4)
		self.p4=Point(2, 5)

	def test_str(self):
		self.assertEqual(self.p1.__str__(), "(1, 1)")

	def test_repr(self):
		self.assertEqual(self.p1.__repr__(), "Point(1, 1)")

	def test_eq(self):
		self.assertEqual(self.p1 == self.p2, False)
		self.assertEqual(self.p1 == self.p1, True)

	def test_ne(self):
		self.assertEqual(self.p1 != self.p1, False)
		self.assertEqual(self.p1 != self.p2, True)

	def test_add(self):
		self.assertEqual(self.p1 + self.p2, Point(2, 1))

	def test_sub(self):
		self.assertEqual(self.p1 - self.p2, Point(0, 1))

	def test_mul(self):
		self.assertEqual(self.p3 * self.p4, 26)
		self.assertEqual(self.p1 * self.p2, 1)

	def test_cross(self):
		self.assertEqual(Point.cross(self.p3, self.p4), 7)

	def test_length(self):
		self.assertEqual(self.p1.length(), math.sqrt(2))
		self.assertEqual(self.p3.length(), 5)

if __name__=='__main__':
    unittest.main()