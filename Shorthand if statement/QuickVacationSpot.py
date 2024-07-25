loves_beach = True
budget = 1500 #Initial budget in dollars
high_budget = budget >= 2000

destination = "beach resort" if loves_beach and not high_budget else "luxurt mountain resort"
budget -= 500 if destination == "beach resort" else 1000 #Compound assingment
#budget = budget - 500

print(destination)
print(f"Remaining budget: {budget}")