from dataclasses import dataclass


@dataclass
class Rectangle:
    length: float
    width: float

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (2 * self.length) + (2 * self.width)
