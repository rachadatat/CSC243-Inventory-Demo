"""Small instructor-only GitHub demonstration, not a complete CSC/BIF243 project."""

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, quantity):
        if quantity < 0:
            return False
        self.products.append(Product(name, quantity))
        return True

    def show_products(self):
        if not self.products:
            print("No products yet.")
        for product in self.products:
            print(f"{product.name}: {product.quantity}")


def main():
    inventory = Inventory()
    inventory.add_product("Notebook", 5)
    inventory.add_product("Pen", 2)
    print("Current inventory:")
    inventory.show_products()


if __name__ == "__main__":
    main()
