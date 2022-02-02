from dataclasses import dataclass
from rectangle import Rectangle
from circle import Circle


@dataclass
class Scene:
    shapes: list

    def add_shape(self, new_shape):
        assert isinstance(new_shape, Circle) or \
               isinstance(new_shape, Rectangle), 'New shape must of type Circle or Rectangle'
        self.shapes.append(new_shape)
