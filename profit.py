actual_cost = float(input("Please write the cost of product: "))
sales_amount = float(input("Please write the new cost of product: "))
if(sales_amount > actual_cost):
    amount = actual_cost-sales_amount
    print("Total profit = {0}".format(amount))
else:
    print("No Profit!!!!!!!")