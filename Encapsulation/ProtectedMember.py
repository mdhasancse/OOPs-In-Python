# Python does not have real protected method 
class shape:
    _length = 10
    _width = 20

class circle(shape):
    def __init__(self):
        print(self._length)
        print(self._width)

obj = circle()
