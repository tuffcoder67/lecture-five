actual_cost = float(input(" Please enter the actual cost: "))
sale_amount = float(input("please enter the sale amount: "))
if (sale_amount > actual_cost):
    print("Total Profit = ",sale_amount - actual_cost)
else:
    print("No Profit!!!!!!!")