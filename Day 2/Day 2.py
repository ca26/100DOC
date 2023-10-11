#This a Tip calcultor project, taking the total bill adding a tip amount, and determining how much each person should pay.

print("Welcome to the tip calc")
bill = float(input("What was the total bill? "))
percent = float(input("What percent tip? 10, 12, 15? "))
people = int(input("how many peolpe? "))
percentnum = percent/100
billtotal = (bill*percentnum)+(bill)
split = round(float(billtotal/people), 2)
print(f"Each person should pay ${split}")
