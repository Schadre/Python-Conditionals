energy_level = 4.5 #Using a float on a scale of 1.0 to 5.0, where 5.0 is very energetic
time_available = 30.5 #using a float to represent minutes availbe for workout
short_on_time = time_available < 45.0 

workout = "intense cardio" if energy_level > 4.0 and not short_on_time else "light yoga"
print(workout)