import random
import json

class Shape:
    """Base class for shapes and fractals."""
    def _init_(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color  # Format (R, G, B)

    def to_dict(self):
        """Method to be redefined in subclasses."""
        raise NotImplementedError("This method must be implemented in subclasses.")


class Circle(Shape):
    """Class for a circle."""
    def _init_(self, x, y, size, color):
        super()._init_(x, y, size, color)

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
    def _init_(self, x, y, size, color):
        super()._init_(x, y, size, color)

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
    def _init_(self, x, y, size, color):
        super()._init_(x, y, size, color)

    def to_dict(self):
        return {
            "type": "triangle",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})"
        }

class Fractal(Shape):
    """Base class for fractals."""
    def _init_(self, x, y, size, color):
        super()._init_(x, y, size, color)

    def to_dict(self):
        """Method to be redefined in subclasses."""
        raise NotImplementedError("This method must be implemented in subclasses.")


class Mandelbrot(Fractal):
    """Class for a Mandelbrot set."""
    def _init_(self, x, y, size, color, max_iter=100):
        super()._init_(x, y, size, color)
        self.max_iter = max_iter  # Maximum iterations for Mandelbrot calculation

    def to_dict(self):
        return {
            "type": "mandelbrot",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})",  # Convert to CSS rgb() format
            "max_iter": self.max_iter
        }


class Julia(Fractal):
    """Class for a Julia set."""
    def _init_(self, x, y, size, color, c_real=-0.4, c_imag=0.6, max_iter=100):
        super()._init_(x, y, size, color)
        self.c_real = c_real  # Real part of the constant C
        self.c_imag = c_imag  # Imaginary part of the constant C
        self.max_iter = max_iter  # Maximum iterations
    def to_dict(self):
        return {
            "type": "julia",
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "color": f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})",  # Convert to CSS rgb() format
            "c_real": self.c_real,
            "c_imag": self.c_imag,
            "max_iter": self.max_iter
        }


def generate_random_fractals(n=10):
    """Génère N formes aléatoires."""
    shapes = []
    for _ in range(n):
        shape_type = random.choice([Circle, Square, Triangle, Mandelbrot, Julia])  # Choix aléatoire de classe
        x = random.randint(50, 350)  # Position X aléatoire
        y = random.randint(50, 350)  # Position Y aléatoire
        size = random.randint(30, 70)  # Taille aléatoire
        color = [random.randint(0, 255) for _ in range(3)]  # Couleur RGB aléatoire

        if shape_type == Mandelbrot:
            max_iter = random.randint(50, 200)  # Random max iterations for fractals
            shape = Mandelbrot(x, y, size, color, max_iter)

        elif shape_type == Julia:
             max_iter = random.randint(50, 200)  # Random max iterations for fractals
             c_real = random.uniform(-1, 1)  # Random real part for Julia set constant
             c_imag = random.uniform(-1, 1)  # Random imaginary part
             shape = Julia(x, y, size, color, c_real, c_imag, max_iter)
        elif shape_type == Circle:
            shape = Circle(x, y, size , color)  # Circle radius is the javascript side will take care of the radius problem.
        elif shape_type == Square:
            shape = Square(x, y, size, color)
        elif shape_type == Triangle:
            shape = Triangle(x, y, size, color)

        shapes.append(shape.to_dict())

    return shapes


# Test - Affichage JSON des formes générées
if __name__== "_main_":
    print(json.dumps(generate_random_fractals(), indent=4))