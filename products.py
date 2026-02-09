class Product:
    """Represents a product in the store inventory."""
    def __init__(self, name, price, quantity):
        """Create a product with name, price, quantity; set active=True; validate inputs."""
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return current product quantity."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Set the product quantity; reactivate if quantity > 0."""
        self.quantity = quantity

    def is_active(self) -> bool:
        """Return whether the product is active (in stock)."""
        return self.quantity > 0

    def buy(self, quantity: int) -> float:
        """Buy quantity units and return total price; decrease stock; deactivate if stock hits 0."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self.quantity:
            raise ValueError("Not enough stock")

        self.quantity -= quantity
        return self.price * quantity

    def show(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"