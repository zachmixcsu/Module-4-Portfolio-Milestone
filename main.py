class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}')

print("item 1")
name = input("Enter the item name: ")
price = float(input("Enter the item price: "))
quantity = int(input("Enter the item quantity: "))
item1 = ItemToPurchase(name, price, quantity)

print("item 2")
name = input("Enter the item name: ")
price = float(input("Enter the item price: "))
quantity = int(input("Enter the item quantity: "))
item2 = ItemToPurchase(name, price, quantity)


print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: ${(item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)}")