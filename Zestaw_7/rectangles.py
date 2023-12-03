from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if(x1 >= x2 or y1 >= y2):
            raise ValueError("Niepoprawne współrzędne wierzchołków")
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

    def intersection(self, other): # część wspólna prostokątów
        p1x = max(self.pt1.x, other.pt1.x)
        p2x = min(self.pt2.x, other.pt2.x)
        p1y = max(self.pt1.y, other.pt1.y)
        p2y = min(self.pt2.y, other.pt2.y)
        
        if(p2x < p1x or p2y < p1y):
            raise ValueError("Prostokąty nie mają części wspólnej")
        
        return Rectangle(p1x, p1y, p2x, p2y)
            

    def cover(self, other):    # prostąkąt nakrywający oba
        p1x = min(self.pt1.x, other.pt1.x)
        p2x = max(self.pt2.x, other.pt2.x)
        p1y = min(self.pt1.y, other.pt1.y)
        p2y = max(self.pt2.y, other.pt2.y)
        
        return Rectangle(p1x,p1y,p2x,p2y)
        

    def make4(self):           # zwraca krotkę czterech mniejszych
    # A-------B   po podziale  A---+---B
    # |       |                |   |   |
    # |       |                +---+---+
    # |       |                |   |   |
    # D-------C                D---+---C

        
        x12 = (self.pt2.x + self.pt1.x)/2
        y12 = (self.pt2.y + self.pt1.y)/2
        
        return [Rectangle(self.pt1.x, self.pt1.y, x12, y12),
                Rectangle(self.pt1.x, y12, x12, self.pt2.y),
                Rectangle(x12, y12, self.pt2.x, self.pt2.y),
                Rectangle(x12, self.pt1.y, self.pt2.x, y12)]
    
    

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
            
        self.rect1 = Rectangle(1, 2, 3, 4)
        self.rect2 = Rectangle(1, 2, 4, 5)
        self.rect3 = Rectangle(2, 3, 5, 6)
        self.rect4 = Rectangle(3, 4, 4, 5)
        self.rect5 = Rectangle(5, 3, 6, 4)
        with self.assertRaises(ValueError) as context:
            self.recte_0 = Rectangle(6, 2, 1, 4)
        with self.assertRaises(ValueError) as context:
            self.recte_1 = Rectangle(1, 2, 1, 4)
        with self.assertRaises(ValueError) as context:
            self.recte_2 = Rectangle(1, 2, 2, 1)
        with self.assertRaises(ValueError) as context:
            self.recte_3 = Rectangle(1, 2, 2, 2)
        with self.assertRaises(ValueError) as context:
            self.recte_4 = Rectangle(4, 4, 2, 2)


    def test_str(self):
        self.assertEqual(self.rect1.__str__(), "[(1, 2), (3, 4)]")	

    def test_repr(self):
        self.assertEqual(self.rect1.__repr__(), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        self.assertEqual(self.rect1 == self.rect1, True)
        self.assertEqual(self.rect1 == self.rect2, False)

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(2, 3))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 4)
        self.assertEqual(self.rect4.area(), 1)

    def test_move(self):
        self.rect1.move(2, 1)
        self.assertEqual(self.rect1, Rectangle(3, 3, 5, 5))

    def test_intersection(self):
        self.assertEqual(self.rect1.intersection(self.rect2), Rectangle(1, 2, 3, 4))
        self.assertEqual(self.rect1.intersection(self.rect3), Rectangle(2, 3, 3, 4))
        self.assertEqual(self.rect3.intersection(self.rect4), Rectangle(3, 4, 4, 5))
        with self.assertRaises(ValueError) as context:
            self.rect1.intersection(self.rect5)

    def test_cover(self):
        self.assertEqual(self.rect1.cover(self.rect2), Rectangle(1, 2, 4, 5))
        self.assertEqual(self.rect1.cover(self.rect5), Rectangle(1, 2, 6, 4))

    def test_make4(self):
        self.assertEqual(self.rect1.make4(), [Rectangle(1, 2, 2, 3), 
            Rectangle(1, 3, 2, 4), Rectangle(2, 3, 3, 4), 
            Rectangle(2, 2, 3, 3)])
        self.assertEqual(self.rect4.make4(), [Rectangle(3, 4, 3.5, 4.5), 
            Rectangle(3, 4.5, 3.5, 5), Rectangle(3.5, 4.5, 4, 5), 
            Rectangle(3.5, 4, 4, 4.5)])
        
if __name__ == '__main__':
	unittest.main()