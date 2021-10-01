loss = float(input())
revenue = float(input())
profit = revenue - loss
if revenue - loss < 0:
    print("Your loss is: ", -profit)
else:
    print("Your profit is: ", profit)
    print("The profit margin is: ", profit / revenue)
    qty = int(input("Number of employee: "))
    print("Profit per employee: ", profit / qty)
