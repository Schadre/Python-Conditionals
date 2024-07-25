"""
You are programming a digital menu for a modern cafè that offers a
variety of dishes catering to different dietary preferences. The cafè wants
to suggest dishes based on whether a customer prefers vegetarian or non-vegetarian
meals and whether they want a sugar-free option. The menu has the following
reccommendation criteria:

- If the customr prefers a vegetarian meal and wants it sugar-free,
suggest a "Fruit salad".
- If the customer prefers a vegetarian meal, but doesn't want it 
sugar-free, suggest a "Veg cake".
- If the customer prefers a non-vegetarian meal and wants it sugar-free
suggest "Sugar-free ice cream".
- For any other combination, suggest a "Chocolate brownie".

Write a Python program that:
- Ask the user about their meal type preference(veg/non-veg)
- Ask the user about their dietary preference(sugar-free/regular)
- Determines the dish based on the above criteria
- Displays the recommended dish to the user """

meal_type = str(input("What is your meal preference?(Vegetarian/Non-Vegetarian): ").lower())
dietary_preference = str(input("What is your dietary preference?(Sugar-free/Regular): ").lower())

if meal_type == "vegetarian":
    if dietary_preference == "sugar-free":
        print(f"I would recommend getting a Fruit salad!")
    elif dietary_preference == "regular":
        print(f"I would recommend a Veg cake!")
elif meal_type == "non-vegetarian":
    if dietary_preference == "sugar-free":
        print(f"I would recommend Sugar-Free ice cream!")
    elif dietary_preference == "regular":
        print(f"I would recommend a Chocolate Brownie!")
else:
    print(f"I would recommend a Chocolate Brownie!")