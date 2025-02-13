import random
import json

class Shape:
    """Base class for shapes."""
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color  # Format (R, G, B)

    def to_dict(self):
        """Method to be redefined in subclasses."""
        raise NotImplementedError("This method must be implemented in subclasses.")


class Circle(Shape):
    """Class for a circle."""
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)

    def to_dict(self):
        return {
            "type": "circle",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})"
        }


class Square(Shape):
    """Class for a square."""
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)

    def to_dict(self):
        return {
            "type": "square",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})"
        }


class Triangle(Shape):
    """Class for an equilateral triangle."""
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)

    def to_dict(self):
        return {
            "type": "triangle",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})"
        }


def generate_random_shapes(n=40):
    """Génère N formes aléatoires."""
    shapes = []
    for _ in range(n):
        shape_type = random.choice([Circle, Square, Triangle])  # Choix aléatoire de classe (sans fractals)
        x = random.randint(50, 350)  # Position X aléatoire
        y = random.randint(50, 350)  # Position Y aléatoire
        size = random.randint(30, 70)  # Taille aléatoire
        color = [random.randint(0, 255) for _ in range(3)]  # Couleur RGB aléatoire

        if shape_type == Circle:
            shape = Circle(x, y, size, color)  # Circle radius is the javascript side will take care of the radius problem.
        elif shape_type == Square:
            shape = Square(x, y, size, color)
        elif shape_type == Triangle:
            shape = Triangle(x, y, size, color)

        shapes.append(shape.to_dict())

    return shapes


# Test - Affichage JSON des formes générées
if __name__ == "__main__":
    print(json.dumps(generate_random_shapes(), indent=4))