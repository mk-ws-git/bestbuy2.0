from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """Return total price after applying promotion to `quantity` of `product`."""
        raise NotImplementedError


class PercentDiscount(Promotion):
    """Percentage discount (e.g., 30% off)."""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        if percent < 0 or percent > 100:
            raise ValueError("percent must be between 0 and 100")
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """Second item at half price (applies per pair)."""

    def apply_promotion(self, product, quantity: int) -> float:
        pairs = quantity // 2
        remainder = quantity % 2
        return pairs * (product.price * 1.5) + remainder * product.price


class ThirdOneFree(Promotion):
    """Buy 2, get 1 free (every 3rd item is free)."""

    def apply_promotion(self, product, quantity: int) -> float:
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price
