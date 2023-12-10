from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if(x1 >= x2 or y1 >= y2):
            raise ValueError("Niepoprawne współrzędne wierzchołków")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
     
    def from_points(points):
        pt1 = points[0]
        pt2 = points[1]
        return Rectangle(pt1.x, pt1.y, pt2.x, pt2.y)

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
        
    @property
    def top(self):
        return self.pt2.y
    
    @property
    def left(self):
        return self.pt1.x
    
    @property
    def bottom(self):
        return self.pt1.y
    
    @property
    def right(self):
        return self.pt2.x
    
    @property
    def width(self):
        return self.pt2.x - self.pt1.x
    
    @property
    def height(self):
        return self.pt2.y - self.pt1.y
    
    @property
    def bottomleft(self):
        return self.pt1
    
    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)
    
    @property
    def topright(self):
        return self.pt2
    
    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)
    
    @property
    def center(self):          # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)