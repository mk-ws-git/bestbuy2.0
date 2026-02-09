from typing import List, Tuple
from products import Product

class Store:
    """Represents a store holding a list of products and supporting orders."""

    def __init__(self, products: List[Product]):
        """Create a store with an initial list of products."""
        self.products = products

    def add_product(self, product: Product) -> None:
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return total quantity of all products in the store."""
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> List[Product]:
        """Return only active products in the store."""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Buy items in shopping_list and return total order price."""
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError("Product is not in this store")
            total_price += product.buy(quantity)
        return total_price

    def start(self) -> None:
        """Start a simple CLI for the store."""
        while True:
            print("\nStore Menu")
            print("1. List all products")
            print("2. Show total quantity in store")
            print("3. Make an order")
            print("4. Quit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                products = self.get_all_products()
                if not products:
                    print("No products in store.")
                    continue
                for i, p in enumerate(products, start=1):
                    print(f"{i}. {p.show()}")

            elif choice == "2":
                print(f"Total quantity in store: {self.get_total_quantity()}")

            elif choice == "3":
                products = self.get_all_products()
                if not products:
                    print("No products in store.")
                    continue

                for i, p in enumerate(products, start=1):
                    print(f"{i}. {p.show()}")

                shopping_list = []
                while True:
                    item = input("Enter product number (or 'done'): ").strip().lower()
                    if item == "done":
                        break

                    if not item.isdigit() or not (1 <= int(item) <= len(products)):
                        print("Invalid product number.")
                        continue

                    qty = input("Enter quantity: ").strip()
                    if not qty.isdigit() or int(qty) <= 0:
                        print("Invalid quantity.")
                        continue

                    product = products[int(item) - 1]
                    shopping_list.append((product, int(qty)))

                if not shopping_list:
                    print("No items ordered.")
                    continue

                try:
                    total = self.order(shopping_list)
                    print(f"Order placed. Total cost: {total}")
                except Exception as e:
                    print(f"Order failed: {e}")

            elif choice == "4":
                print("Goodbye.")
                return

            else:
                print("Invalid choice.")
