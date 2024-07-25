""" Task 3: Catering Choices

Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" 
if yes, otherwise recommend "Gourmet Meals Caterers". """

food_type = str(input("Do you want vegetarian food? (yes/no)").lower())

print("I recommend Veggie Delight Caterers! ^_^ ") if food_type == "yes" else print("Gourmet Meals Caterers! ^_^")

