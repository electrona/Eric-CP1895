class Product:
    def __init__(self, name, price, discount_percent):
        self.name = name
        self.price = price
        self.discountPercent = discount_percent

    def get_discount_amount(self):
        return self.price * self.discountPercent / 100

    def get_discount_price(self):
        discount_amount = self.price * self.discountPercent / 100
        return self.price - discount_amount


def main():
    product1 = Product("Stanley 13 Ounce Wood Hammer", 12.99, 62)

    product2 = Product("National Hardware 3/4\" Wire Nails", 5.06, 0)

    print("PRODUCTS")
    print("=" * 8)
    print()

    print(f"Name: {product1.name}")
    print(f"Price: ${product1.price:.2f}")
    print(f"Discount: {product1.discountPercent}%")
    print(f"Discount Price: ${product1.get_discount_price():.2f}")
    print(f"Discount Amount: ${product1.get_discount_amount():.2f}")
    print()
    print(f"Name: {product2.name}")
    print(f"Price: ${product2.price:.2f}")
    print(f"Discount Percent: {product2.discountPercent}%")
    print(f"Discount Price: ${product2.get_discount_price():.2f}")
    print(f"Discount Amount: ${product2.get_discount_amount():.2f}")


if __name__ == "__main__":
    main()
