# Task 1 Restarurant Menu Update: You are given an initial structure of a restarunt menu stored in a nested 
#dictionary. Your task is to update this menu by: adding a new category called "Beverages" with at least two items,
#update the price of "Steak" to 17.99, and remove "Bruschetta" from "Starters".

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

print(restaurant_menu)

restaurant_menu["Beverages"] = {"Water": 0.49, "Coca-cola": 1.99, "Oragne Soda": 1.99}

restaurant_menu["Main Course"].update({"Steak": 17.99})

del restaurant_menu["Starters"]["Bruschetta"]
print(f"\n{restaurant_menu}")
