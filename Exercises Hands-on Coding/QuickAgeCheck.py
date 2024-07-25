"""
You are programming a digital bouncer for an online game portal.
The portal games that are only suitable for players aged 18 and above.  
You need to ensure that players meet the age requirements beforethey can
access these games. The bouncer has the following criteria:

- If the player's age is 18 or above, display "You can drive!".
- If the player's age is below 18, display "Not yet!"

Write a Python program that:
- Ask the user for their age
- Determines if the user is old enough to access the games based on the
above criteria
- Displays the appropriate message to the user. 

** Hint: Use nested if statements to determine the message based on the 
user's age. """

age = int(input("How old are you? "))
# if age >= 18:
#     print(f"You can drive!")
# elif age < 18:
#     print(f"Not yet!")
print(f"You can drive!") if age >= 18 else print(f"Not yet!")
