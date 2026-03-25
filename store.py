from collections import defaultdict
from typing import List, Tuple
from products import LimitedProduct, NonStockedProduct, Product


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
        aggregated_quantities = defaultdict(int)

        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError("Product is not in this store")
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            aggregated_quantities[product] += quantity

        for product, total_quantity in aggregated_quantities.items():
            if (
                isinstance(product, LimitedProduct)
                and total_quantity > product.maximum
            ):
                raise ValueError("Exceeded maximum allowed per order")
            if (
                not isinstance(product, NonStockedProduct)
                and total_quantity > product.get_quantity()
            ):
                raise ValueError("Not enough stock")

        total_price = 0.0
        for product, total_quantity in aggregated_quantities.items():
            total_price += product.buy(total_quantity)

        return total_price
