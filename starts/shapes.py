import random
import json

class Shape:
    """Classe de base pour les formes."""
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color  # Format (R, G, B)

    def to_dict(self):
        """Méthode à redéfinir dans les sous-classes."""
        raise NotImplementedError("Cette méthode doit être implémentée dans les sous-classes.")


class Circle(Shape):
    """Classe pour un cercle."""
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color)
        self.radius = radius

    def to_dict(self):
        return {
            "type": "circle",
            "x": self.x,
            "y": self.y,
            "radius": self.radius,
            "color": self.color
        }


class Square(Shape):
    """Classe pour un carré."""
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)

    def to_dict(self):
        return {
            "type": "square",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": self.color
        }


class Triangle(Shape):
    """Classe pour un triangle équilatéral."""
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)

    def to_dict(self):
        return {
            "type": "triangle",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": self.color
        }


def generate_random_shapes(n=10):
    """Génère N formes aléatoires."""
    shapes = []
    for _ in range(n):
        shape_type = random.choice([Circle, Square, Triangle])  # Choix aléatoire de classe
        x = random.randint(50, 350)  # Position X aléatoire
        y = random.randint(50, 350)  # Position Y aléatoire
        size = random.randint(30, 70)  # Taille aléatoire
        color = [random.randint(0, 255) for _ in range(3)]  # Couleur RGB aléatoire

        if shape_type == Circle:
            shape = Circle(x, y, size // 2, color)  # Le radius est size / 2
        else:
            shape = shape_type(x, y, size, color)

        shapes.append(shape.to_dict())

    return shapes


# Test - Affichage JSON des formes générées
if __name__ == "__main__":
    print(json.dumps(generate_random_shapes(), indent=4))
