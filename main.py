import products
import promotions
import store


def create_store():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    return store.Store(product_list)


def print_menu():
    print("\nStore Menu")
    print("1. List all products")
    print("2. Show total quantity in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(best_buy):
    product_list = best_buy.get_all_products()
    if not product_list:
        print("No products in store.")
        return []

    for index, product in enumerate(product_list, start=1):
        print(f"{index}. {product.show()}")
    return product_list


def show_total_quantity(best_buy):
    print(f"Total quantity in store: {best_buy.get_total_quantity()}")


def collect_shopping_list(product_list):
    shopping_list = []

    while True:
        item = input("Enter product number (or 'done'): ").strip().lower()
        if item == "done":
            break

        if not item.isdigit() or not (1 <= int(item) <= len(product_list)):
            print("Invalid product number.")
            continue

        qty = input("Enter quantity: ").strip()
        if not qty.isdigit() or int(qty) <= 0:
            print("Invalid quantity.")
            continue

        selected_product = product_list[int(item) - 1]
        shopping_list.append((selected_product, int(qty)))

    return shopping_list


def make_order(best_buy):
    product_list = list_products(best_buy)
    if not product_list:
        return

    shopping_list = collect_shopping_list(product_list)
    if not shopping_list:
        print("No items ordered.")
        return

    try:
        total = best_buy.order(shopping_list)
        print(f"Order placed. Total cost: {total}")
    except Exception as error:
        print(f"Order failed: {error}")


def start(best_buy):
    """Start a simple CLI for the store."""
    while True:
        print_menu()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            list_products(best_buy)
        elif choice == "2":
            show_total_quantity(best_buy)
        elif choice == "3":
            make_order(best_buy)
        elif choice == "4":
            print("Goodbye.")
            return
        else:
            print("Invalid choice.")


def main():
    best_buy = create_store()
    start(best_buy)


if __name__ == "__main__":
    main()
