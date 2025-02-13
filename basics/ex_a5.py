price=1000000
good_credit=False
bad_credit=True
if good_credit:
    price=(10/100)*price
else:
    price=(20/100)*price
print(f'''The down payment is Rs.{price}''')