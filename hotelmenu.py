# Define the menu of the cafe
menu = {
    "Cold Coffee": 150,
    "Lava Cake": 125,
    "Hot Coffee": 110,
    "Cookies": 99,
    "Croissant": 75,
    "Ice tea": 59,
    "Choco chips shake": 178
}

# Greet message
print("Welcome to the Python cafe")
print("Cold Coffee: Rs150\nLava Cake: Rs125\nHot Coffee: Rs110\nCookies: Rs99\nCroissant: Rs75\nIce tea: Rs59\nChoco chips shake: Rs178")

# creating the variable to store the total amount of the order
order_total = 0

item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of your second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")  
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")                  

