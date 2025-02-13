#calculates total cost of shopping items in cart
fanta_100ml=140
rice_10kg=3000
flour_5kg=1794
chips_50g=50

items_name=['fanta_100ml','rice_10kg','flour_5kg','chips_50g']
items_price=[fanta_100ml,rice_10kg,flour_5kg,chips_50g]

print("Total items:")

total_price=0
for i in range(len(items_name)):
            print(f"#{i+1} {items_name[i]}-----Rs.{items_price[i]} ")
            total_price+=items_price[i]

print(f"Total price={total_price}")
