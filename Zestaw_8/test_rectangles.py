# Kod testujący moduł.

from points import Point
from rectangles import Rectangle



rectangle1 = Rectangle(1, 2, 3, 4)

rectangle2 = Rectangle(1, 2, 4, 5)

def test_from_points():
    assert Rectangle.from_points((Point(1, 2), Point(3, 4))) == rectangle1

def test_str():
    assert str(rectangle1) == "[(1, 2), (3, 4)]"
    
def test_repr():
    assert repr(rectangle1) == "Rectangle(1, 2, 3, 4)"
    
def test_eq():
    assert (rectangle1 == rectangle1) == True
    assert (rectangle1 == rectangle2) == False
    
def test_center():
    assert rectangle1.center == Point(2,3)
    
def test_area():
    assert rectangle1.area() == 4
    
def test_move():
    rectangle = Rectangle(1, 2, 3, 4)
    rectangle.move(2, 1)
    assert rectangle == Rectangle(3, 3, 5, 5)
    
def test_intersection():
    assert rectangle1.intersection(rectangle2) == Rectangle(1, 2, 3, 4)
    
def test_cover():
    assert rectangle1.cover(rectangle2) == Rectangle(1, 2, 4, 5)
    
def test_make4():
    assert rectangle1.make4() == [Rectangle(1, 2, 2, 3), 
            Rectangle(1, 3, 2, 4), Rectangle(2, 3, 3, 4), 
            Rectangle(2, 2, 3, 3)]
    
def test_coordinates():
    assert rectangle1.top == 4
    assert rectangle1.bottom == 2
    assert rectangle1.right == 3
    assert rectangle1.left == 1
    assert rectangle1.height == 2
    assert rectangle1.width == 2
    
def test_points():
    assert rectangle1.bottomleft == Point(1, 2)
    assert rectangle1.bottomright == Point(3, 2)
    assert rectangle1.topright == Point(3, 4)
    assert rectangle1.topleft == Point(1, 4)
    
