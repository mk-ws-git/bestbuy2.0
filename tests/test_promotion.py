import pytest

from bestbuy.products import Product, NonStockedProduct, LimitedProduct
from bestbuy.promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


def test_percent_discount_applies_correctly():
    p = Product("A", price=100, quantity=10)
    p.set_promotion(PercentDiscount("30% off", percent=30))
    assert p.buy(2) == 140  # 2 * 100 * 0.7
    assert p.get_quantity() == 8


def test_second_half_price_applies_correctly_even_quantity():
    p = Product("A", price=10, quantity=10)
    p.set_promotion(SecondHalfPrice("Second half"))
    assert p.buy(2) == 15  # 10 + 5
    assert p.get_quantity() == 8


def test_second_half_price_applies_correctly_odd_quantity():
    p = Product("A", price=10, quantity=10)
    p.set_promotion(SecondHalfPrice("Second half"))
    assert p.buy(3) == 25  # (10 + 5) + 10
    assert p.get_quantity() == 7


def test_third_one_free_applies_correctly():
    p = Product("A", price=10, quantity=10)
    p.set_promotion(ThirdOneFree("3rd free"))
    assert p.buy(3) == 20  # pay for 2
    assert p.get_quantity() == 7


def test_promotion_on_non_stocked_product_does_not_change_quantity():
    p = NonStockedProduct("License", price=100)
    p.set_promotion(PercentDiscount("30% off", percent=30))
    assert p.buy(2) == 140
    assert p.get_quantity() == 0
    assert p.is_active() is True


def test_limited_product_still_enforces_maximum_with_promotion():
    p = LimitedProduct("Shipping", price=10, quantity=10, maximum=1)
    p.set_promotion(PercentDiscount("50% off", percent=50))

    assert p.buy(1) == 5
    assert p.get_quantity() == 9

    with pytest.raises(Exception):
        p.buy(2)
