from .shape import Shape, glColor3f, glBegin, glVertex2f, glEnd, GL_QUADS


class Rectangle(Shape):
    def __init__(self, x, y, width, height, color:tuple[float, float, float]=(1.0, 1.0, 1.0), batch=None):
        super().__init__(batch)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        r, g, b = self.color
        glColor3f(r, g, b)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.width, self.y)
        glVertex2f(self.x + self.width, self.y + self.height)
        glVertex2f(self.x, self.y + self.height)
        glEnd()