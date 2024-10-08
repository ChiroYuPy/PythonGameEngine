from OpenGL.GL import glVertex2f, glBegin, glColor3f, glEnd, GL_QUADS, GL_TRIANGLE_FAN


class Shape:
    def __init__(self, batch):
        if batch is not None:
            batch.add_shape(self)

    def draw(self):
        raise NotImplementedError('Draw method must be implemented')