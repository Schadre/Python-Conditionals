"""
Objective: To practice the use of shorthand if statements.

Task 1: Code Correction You are provided with a Python script 
that is supposed to help in event planning, but it has errors. 
Identify and fix them.

Task 2: Venue Selection
Based on the corrected code from Task 1, further enhance your 
code to recommend additional things like "audio system" or "projector" 
based on the number of attendees.

Task 3: Catering Choices
Ask the user if they want "vegetarian" food. 
Recommend "Veggie Delight Caterers" if yes, 
otherwise recommend "Gourmet Meals Caterers".

"""
attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)
if attendees > 100:
    projector = str(input("Would you like an projector?(yes/no)").lower())
    if projector == "yes":
        print("There will be a projector setup upon arrival for you and all your guest, thank you for booking with us!")
    else:
        print("We have confirmed your reservation for a large hall without a projector, thank you for booking with us!")
elif attendees < 100:
    audio = str(input("Would you like an audio system?(yes/no)").lower())
    if audio == "yes":
        print("There will be an audio system setup upon arrival for you and all your guest, thank you for booking with us!")
    else:
        print("We have confirmed your reservation for a conference room without an audio system, thank you for booking with us!")

food_type = str(input("Do you want vegetarian food? (yes/no)").lower())

print("I recommend Veggie Delight Caterers! ^_^ ") if food_type == "yes" else print("Gourmet Meals Caterers! ^_^")


