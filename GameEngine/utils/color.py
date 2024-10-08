class Color:
    def __init__(self, r, g, b, a=1.0):
        self.r = max(0.0, min(1.0, r))
        self.g = max(0.0, min(1.0, g))
        self.b = max(0.0, min(1.0, b))
        self.a = max(0.0, min(1.0, a))

    def to_hex(self):
        return "#{:02x}{:02x}{:02x}{:02x}".format(
            int(self.r * 255),
            int(self.g * 255),
            int(self.b * 255),
            int(self.a * 255)
        )

    @classmethod
    def from_hex(cls, hex_color):
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 6:  # RGB
            r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
            return cls(r / 255, g / 255, b / 255)
        elif len(hex_color) == 8:  # RGBA
            r, g, b, a = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4, 6))
            return cls(r / 255, g / 255, b / 255, int(a / 255))
        else:
            raise ValueError("Invalid HEX color format")

    def mix(self, other, ratio=0.5):
        r = self.r * (1 - ratio) + other.r * ratio
        g = self.g * (1 - ratio) + other.g * ratio
        b = self.b * (1 - ratio) + other.b * ratio
        a = self.a * (1 - ratio) + other.a * ratio
        return Color(r, g, b, a)

    def __repr__(self):
        return f"Color(r={self.r}, g={self.g}, b={self.b}, a={self.a})"
