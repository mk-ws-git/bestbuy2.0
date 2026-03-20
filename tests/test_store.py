import pytest

from products import Product, NonStockedProduct, LimitedProduct
from store import Store


@pytest.fixture
def sample_store():
    p1 = Product("Laptop", price=1000, quantity=10)
    p2 = Product("Headphones", price=200, quantity=5)
    p3 = NonStockedProduct("License", price=50)
    p4 = LimitedProduct("Shipping", price=10, quantity=100, maximum=1)
    return Store([p1, p2, p3, p4])


def test_order_single_item_returns_correct_total(sample_store):
    laptop = sample_store.get_all_products()[0]
    total = sample_store.order([(laptop, 2)])
    assert total == 2000


def test_order_multiple_items_returns_combined_total(sample_store):
    products = sample_store.get_all_products()
    laptop = products[0]      # price=1000
    headphones = products[1]  # price=200
    total = sample_store.order([(laptop, 1), (headphones, 2)])
    assert total == 1400  # 1*1000 + 2*200


def test_order_multiple_items_reduces_stock_for_all(sample_store):
    products = sample_store.get_all_products()
    laptop = products[0]
    headphones = products[1]
    sample_store.order([(laptop, 3), (headphones, 2)])
    assert laptop.get_quantity() == 7
    assert headphones.get_quantity() == 3


def test_order_raises_for_product_not_in_store():
    store = Store([Product("A", price=10, quantity=5)])
    other = Product("B", price=10, quantity=5)
    with pytest.raises(Exception):
        store.order([(other, 1)])


def test_order_raises_when_quantity_exceeds_stock(sample_store):
    headphones = sample_store.get_all_products()[1]  # quantity=5
    with pytest.raises(Exception):
        sample_store.order([(headphones, 10)])


def test_order_raises_for_limited_product_exceeding_maximum(sample_store):
    shipping = sample_store.get_all_products()[3]
    with pytest.raises(Exception):
        sample_store.order([(shipping, 2)])


def test_order_same_product_twice_aggregates_quantity(sample_store):
    laptop = sample_store.get_all_products()[0]  # quantity=10
    total = sample_store.order([(laptop, 3), (laptop, 4)])
    assert total == 7000  # 7 * 1000
    assert laptop.get_quantity() == 3
