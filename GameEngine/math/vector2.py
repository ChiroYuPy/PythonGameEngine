from .functions import sqrt


class Vector2:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return Vector2(self.x // other, self.y // other)

    def __mod__(self, other):
        return Vector2(self.x % other, self.y % other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __neg__(self):
        return Vector2(-self.x, -self.y)