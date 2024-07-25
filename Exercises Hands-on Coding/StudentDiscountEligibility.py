""" 
A school offers various discounts to its students based on their 
academic performance and participation in extracurricular activities.
The discount criteria are as follows:

- Students with a grade of "A" and who are also part of the 
schools sports team get a 20% discount.
- Student with a grade of "A" but not in the sports team get a
10% discount. 
- Students with a grade of "B" and who are part of the schools
drama club get a 15% discount. 

Write a Python program that:
- Ask the user for their grade (A/B/C)
- Ask if they are part of the sports team(yes/no)
- Ask if they are part of the drama club(yes/no)
- Determines the discount percentage based on the above criteria
- Displays the discount percentage to the user

** Hint: Use nested if statements to determine the discount percentage 
based on the student's grade and extracurricular activities"""

grade = str(input("What is your grade?(A/B/C) ").lower())
sports_team = str(input("Are you apart of the sports team?(yes/no) ").lower())
drama_club = str(input("Are you apart of the drama club?(yes/no) ").lower())

if grade == "a":
    if sports_team == "yes":
        print(f"You will receive a 20% discount! Congrats!")
    elif sports_team == "no":
        print(f"You will receive a 10% discount! Congrats!")
elif grade == "b":
    if sports_team == "yes":
        print(f"You will receive a 15% discount! Congrats!")
    elif sports_team == "no":
        print(f"Sadly, there are no discounts available for your current status.")
else:
     print(f"Sadly, there are no discounts available for your current status.")