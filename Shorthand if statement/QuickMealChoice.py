current_hour = 15 #Using an integer to represent the hour in 24 hour format
hunger_level = 7 #Using an integer on a scale of 1 to 10, where 10 is extremel hungry

meal = "snack" if current_hour < 17 and hunger_level < 5 else "full meal"
print(meal)