from circle import Circle
from rectangle import Rectangle
from scene import Scene


def main():
    circle = Circle(radius=15.5)
    rectangle = Rectangle(length=20.2, width=10.1)
    scene = Scene(shapes=[])
    scene.add_shape(circle)
    scene.add_shape(rectangle)
    print(scene)


if __name__ == "__main__":
    main()
