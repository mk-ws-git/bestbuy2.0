import pytest

from bestbuy.products import Product

def test_invalid_product_empty_name_raises_exception():
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)


def test_invalid_product_negative_price_raises_exception():
    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_when_quantity_reaches_zero():
    p = Product("USB Cable", price=10, quantity=1)
    assert p.is_active() is True

    p.buy(1)

    assert p.get_quantity() == 0
    assert p.is_active() is False


def test_valid_purchase_updates_quantity_and_returns_total_price():
    p = Product("Keyboard", price=50, quantity=10)

    result = p.buy(3)

    assert p.get_quantity() == 7
    assert result == 150  # 3 * 50


def test_over_purchase_raises_exception():
    p = Product("Mouse", price=25, quantity=2)

    with pytest.raises(Exception):
        p.buy(3)