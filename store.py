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
