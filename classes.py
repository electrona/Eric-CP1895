class Lightbulb:
    def __init__(self, wattage, brightness, is_led, brand, is_on=False):
        self.wattage = wattage
        self.brightness = brightness
        self.is_led = is_led
        self.brand = brand
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True
        print("Light is on!")

    def turn_off(self):
        self.is_on = False
        print("Light is off")

    def to_string(self):
        print(f"Wattage: {self.wattage}")
        print(f"Brightness: {self.brightness}")
        print(f"Is LED: {self.is_led}")
        print(f"Brand: {self.brand}")
        print(f"Is on: {self.is_on}")

    def set_brightness(self, brightness):
        self.brightness = brightness
        print(f"Brightness set to {brightness}")


def main():
    lightbulb = Lightbulb(100, 100, True, "Philips")
    lightbulb.to_string()


if __name__ == "__main__":
    main()
