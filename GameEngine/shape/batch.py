class Batch:
    def __init__(self):
        self.shapes = set()

    def add_shape(self, shape):
        self.shapes.add(shape)

    def draw(self):
        for shape in self.shapes:
            shape.draw()