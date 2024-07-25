hour_of_day = 7 #Using an integer to represent the hour in 24-hour format
energy_level = 3 #Using an integer on a scale of 1 to 5, where 5 is very energetic

beverage = "coffee" if (6 <= hour_of_day < 12) and energy_level < 4 else "tea"
print(beverage)

