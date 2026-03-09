import products
import store
import promotions

def main():
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


def start(best_buy):
    """Start a simple CLI for the store."""
    while True:
        print("\nStore Menu")
        print("1. List all products")
        print("2. Show total quantity in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            product_list = best_buy.get_all_products()
            if not product_list:
                print("No products in store.")
                continue
            for i, p in enumerate(product_list, start=1):
                print(f"{i}. {p.show()}")

        elif choice == "2":
            print(f"Total quantity in store: {best_buy.get_total_quantity()}")

        elif choice == "3":
            product_list = best_buy.get_all_products()
            if not product_list:
                print("No products in store.")
                continue

            for i, p in enumerate(product_list, start=1):
                print(f"{i}. {p.show()}")

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

                product = product_list[int(item) - 1]
                shopping_list.append((product, int(qty)))

            if not shopping_list:
                print("No items ordered.")
                continue

            try:
                total = best_buy.order(shopping_list)
                print(f"Order placed. Total cost: {total}")
            except Exception as e:
                print(f"Order failed: {e}")

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