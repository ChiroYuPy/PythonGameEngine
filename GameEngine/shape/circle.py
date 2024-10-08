from .shape import Shape, glColor3f, glBegin, glVertex2f, glEnd, GL_TRIANGLE_FAN
from ..math import PI, cos, sin


class Circle(Shape):
    def __init__(self, x, y, radius, color=(0.0, 0.0, 1.0), num_segments=30, batch=None):
        super().__init__(batch)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.num_segments = num_segments

    def draw(self):
        r, g, b = self.color
        glColor3f(r, g, b)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.x, self.y)
        for i in range(self.num_segments + 1):
            angle = 2 * PI * i / self.num_segments
            dx = self.radius * cos(angle)
            dy = self.radius * sin(angle)
            glVertex2f(self.x + dx, self.y + dy)
        glEnd()