menu = {
    'pizza':40,
    'pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
    'Tea_cup ': 20,
    'Bread_pokra':60
}
#greeting the customer
print("Welcome to the python resturant")
print("pizza:40\npasta:50\nBurger:60\nSalad:70\ncoffee:80\nTea_cup:20\nBread_pokra:60")

order_total = 0

# taking the input from the user
item1 = input("Enter the name of item you want to order = ")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been added to your order")
else:
    print("ordered item {item1} is not available yet")
another_order = input("Do you want to order add another item?(yes/no)")
if another_order == "yes":
    item2 = input("Enter the name of second item = ")
    order_total += menu[item2]
    print("item {item2} has been add to your item = ")
else:
    print("Ordered item{item2}is not available")
print(f"The total amount of the item is {order_total}")