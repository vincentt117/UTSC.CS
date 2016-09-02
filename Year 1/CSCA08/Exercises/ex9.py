import math


class Parallelogram():
    ''' A class which represents a 2D parallelogram'''

    def __init__(self, base, side, theta):
        '''(Parallelogram, int) -> NoneType
        Creates a parallelogram with the given dimensions
        REQ: all three dimensions must be positive values
        REQ: theta < 180
        '''
        self._base = base
        self._side = side
        self._theta = theta

    def __str__(self):
        '''(Parallelogram) -> str
        Returns the identity of this parallelogram with its area
        '''
        return "I am a " + type(self).__name__ + " with area " \
               + str(self.area())

    def area(self):
        '''(Parallelogram) -> float
        Returns the area of this parallelogram
        '''
        return self._base * self._side * math.sin(math.radians(self._theta))

    def bst(self):
        '''(Parallelogram) -> list of floats
        Returns the dimensions and angle of this parallelogram
        '''
        return [self._base, self._side, self._theta]


class Rectangle(Parallelogram):
    ''' A class which represents a 2D rectangle '''
    def __init__(self, base, side):
        '''(Rectangle, float) -> NoneType
        Creates a new rectangle with the given base and side lengh
        REQ: both dimensions are positive
        '''
        Parallelogram.__init__(self, base, side, 90)


class Square(Parallelogram):
    ''' A class which represents a 2D square '''
    def __init__(self, base):
        '''(Square, float) -> NoneType
        Creates a new square with the given base
        REQ: base > 0
        '''
        Parallelogram.__init__(self, base, base, 90)


class Rhombus(Parallelogram):
    ''' A class that represents a 2D rhombus'''
    def __init__(self, base, theta):
        '''(Rhombus, float, float -> NoneType
        Creates a rhombus with the given dimensions
        REQ: base > 0
        REQ: 0 < theta < 180
        '''
        Parallelogram.__init__(self, base, base, theta)
