# ---------- SMART GROCERY BILLING SYSTEM ----------

# Step 1: Store the store's menu as a dictionary.
# Key = item name (string), Value = price per unit (int)
menu = {
    "apple": 50,
    "milk": 60,
    "bread": 40,
    "eggs": 90,
    "rice": 120
}

print("Welcome to the Smart Grocery Billing System")
print("Available items and prices:", menu)
print()

# Step 2: Get details for Item 1 from the user
item1 = input("Enter first item name: ").lower()
qty1 = int(input("Enter quantity for " + item1 + ": "))

# Step 3: Get details for Item 2 from the user
item2 = input("Enter second item name: ").lower()
qty2 = int(input("Enter quantity for " + item2 + ": "))

# Step 4: Get details for Item 3 from the user
item3 = input("Enter third item name: ").lower()
qty3 = int(input("Enter quantity for " + item3 + ": "))

# Step 5: Look up each item's price in the dictionary.
# .get(item, 0) returns 0 if the item isn't found, instead of crashing.
price1 = menu.get(item1, 0)
price2 = menu.get(item2, 0)
price3 = menu.get(item3, 0)

# Step 6: Calculate the cost of each item (price * quantity)
cost1 = price1 * qty1
cost2 = price2 * qty2
cost3 = price3 * qty3

# Step 7: Store each purchase as a tuple: (name, quantity, cost)
# Tuples are used because a finished purchase record shouldn't change.
record1 = (item1, qty1, cost1)
record2 = (item2, qty2, cost2)
record3 = (item3, qty3, cost3)

# Step 8: Put all three records into a list called "cart"
cart = [record1, record2, record3]

# Step 9: Calculate the total bill using arithmetic operators
total = cost1 + cost2 + cost3

# Step 10: Apply a discount using conditionals
if total >= 500:
    discount = total * 0.10          # 10% discount
    discount_msg = "10% discount applied (total >= 500)"
elif total >= 300:
    discount = total * 0.05          # 5% discount
    discount_msg = "5% discount applied (total >= 300)"
else:
    discount = 0
    discount_msg = "No discount applied"

final_total = total - discount

# Step 11: Print the final receipt
print("\n----------- RECEIPT -----------")
print("Cart details:", cart)
print()

if price1 == 0:
    print(item1, "was not found in the menu, so it's charged as 0.")
if price2 == 0:
    print(item2, "was not found in the menu, so it's charged as 0.")
if price3 == 0:
    print(item3, "was not found in the menu, so it's charged as 0.")

print("Subtotal: Rs.", total)
print(discount_msg)
print("Discount Amount: Rs.", discount)
print("Final Total to Pay: Rs.", final_total)
print("--------------------------------")
