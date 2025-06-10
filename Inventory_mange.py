#  CONTENTS
#  1.Overview
#  2.Product Details
#  3.Updating Inventory
#  4.Add Functionalities
#  5.Generating Sales
#  6.Conclusion


# 1. Product Details
with open('products.txt', 'w') as f:
    f.write("101,Apple,50\n")
    f.write("102,Banana,30\n")

# 2. Updating Inventory
product_id = '101'
new_quantity = 45

lines = []
with open('products.txt', 'r') as f:
    lines = f.readlines()

with open('products.txt', 'w') as f:
    for line in lines:
        pid, name, qty = line.strip().split(',')
        if pid == product_id:
            f.write(f"{pid},{name},{new_quantity}\n")
        else:
            f.write(line)

# 3. Add Functionalities
with open('products.txt', 'a') as f:
    f.write("103,Orange,40\n")

# 4. Generating Sales
sales = [("101", 2), ("102", 5)]

# Load inventory into dictionary
inventory = {}
with open('products.txt', 'r') as f:
    for line in f:
        pid, name, qty = line.strip().split(',')
        inventory[pid] = [name, int(qty)]

# Update inventory based on sales
for pid, qty_sold in sales:
    if pid in inventory:
        inventory[pid][1] -= qty_sold  # reduce quantity

# Write updated inventory back to file
with open('products.txt', 'w') as f:
    for pid, (name, qty) in inventory.items():
        f.write(f"{pid},{name},{qty}\n")

# Write sales to a file
with open('sales.txt', 'w') as f:
    for pid, qty_sold in sales:
        f.write(f"Sold {qty_sold} units of Product ID {pid}\n")
