import math
from dataclasses import dataclass


@dataclass
class Circle:
    radius: float

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_circumference(self):
        return 2 * math.pi * self.radius
