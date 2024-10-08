from GameEngine.components import Component
from GameEngine.math.vector2 import Vector2


class RigidBody(Component):
    def __init__(self, velocity: Vector2, acceleration: Vector2, mass: float):
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = mass