class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}')

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="january 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self, itemName):
        found = False
        for item in self.cart_items:
            if item.item_name == itemName:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, itemToPurchase):
        for item in self.cart_items:
            if item.item_name == itemToPurchase.item_name:
                if itemToPurchase.item_price != 0.0:
                    item.item_price = itemToPurchase.item_price
                if itemToPurchase.item_quantity != 0:
                    item.item_quantity = itemToPurchase.item_quantity
                if itemToPurchase.item_description != "none":
                    item.item_description = itemToPurchase.item_description
                return
        print("Item not found in cart. Nothing has been modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_quantity * item.item_price for item in self.cart_items)

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")

        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")



def print_menu(shopping_cart):
    print(("-----------------------"))
    print((" "))
    print("     MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("   q - Quit")
    print(("-----------------------"))
    print((" "))
    option = ''
    while option != 'q':

        print(" ")
        option = input("Choose an option: ")
        print(" ")

        if option == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_description = input("Enter the item description: ")
            item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            shopping_cart.add_item(item_to_purchase)
        elif option == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif option == 'c':
            print("CHANGE ITEM QUANTITY")
            shopping_cart.modify_item(item_name)
        elif option == 'i':
            shopping_cart.print_descriptions()
        elif option == 'o':
            shopping_cart.print_total()
        elif option == 'q':
            print("Quitting...")
        else:
            print("Invalid option, please try again")


def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()



