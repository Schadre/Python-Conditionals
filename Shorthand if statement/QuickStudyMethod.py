topic_difficulty = "hard"
available_hours = 3.5 #Using a float to represent hours available for study
understanding_level = 6 #Using an integer on a scale of 1 to 10, where 10 is full understanding 

study_method = "deep dive" if topic_difficulty == "hard" and available_hours > 2.5 else "quick review"
bonus_hours = 1.5 if understanding_level < 5 else 0.5 #Compound assingment

available_hours += bonus_hours # available_hours = available_hours + bonus_hours

print(study_method)
print(f"Total study hours: {available_hours}")