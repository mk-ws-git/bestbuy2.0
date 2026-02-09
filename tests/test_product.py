import pytest

from products import Product, NonStockedProduct, LimitedProduct

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


def test_non_stocked_product_quantity_is_always_zero():
    p = NonStockedProduct("Windows License", price=125)
    assert p.get_quantity() == 0


def test_non_stocked_product_is_active_even_with_zero_quantity():
    p = NonStockedProduct("Windows License", price=125)
    assert p.is_active() is True


def test_non_stocked_product_buy_does_not_change_quantity_and_returns_total():
    p = NonStockedProduct("Windows License", price=125)

    total = p.buy(3)

    assert total == 375
    assert p.get_quantity() == 0
    assert p.is_active() is True


def test_limited_product_cannot_be_bought_above_maximum():
    p = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    with pytest.raises(Exception):
        p.buy(2)


def test_limited_product_buy_at_or_below_maximum_works_and_reduces_stock():
    p = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    total = p.buy(1)

    assert total == 10
    assert p.get_quantity() == 249