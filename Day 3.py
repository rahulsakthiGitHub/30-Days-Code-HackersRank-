
meal_cost=float(input())
tip_percent=int(input())
tax_percent=int(input())
total_cost=int()
tip=float()
tax=float()

tip=meal_cost/100*tip_percent
tax=tax_percent/100*meal_cost
total_cost=(meal_cost+tip+tax+0.5)

print(int(total_cost))
