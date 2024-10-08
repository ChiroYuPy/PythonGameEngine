from .component import Component
from ..math.vector2 import Vector2


class Transform(Component):
    def __init__(self, position: Vector2, rotation: Vector2, scale: Vector2):
        self.position = position
        self.rotation = rotation
        self.scale = scale