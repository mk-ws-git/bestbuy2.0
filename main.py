import products
import store


def start(best_buy: store.Store):
    """Run the CLI menu for the given store."""
    while True:
        print("\nStore Menu")
        print("-----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            all_products = best_buy.get_all_products()
            for i, product in enumerate(all_products, start=1):
                print(f"{i}. {product.show()}")

        elif choice == "2":
            total = best_buy.get_total_quantity()
            print(f"Total amount in store: {total}")

        elif choice == "3":
            shopping_list = []
            all_products = best_buy.get_all_products()

            for i, product in enumerate(all_products, start=1):
                print(f"{i}. {product.show()}")

            while True:
                product_number = input("Enter product number to buy (or empty to finish): ")
                if product_number == "":
                    break

                quantity = int(input("Enter quantity: "))
                product = all_products[int(product_number) - 1]
                shopping_list.append((product, quantity))

            total_price = best_buy.order(shopping_list)
            print(f"Order cost: {total_price} dollars.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)
    start(best_buy)