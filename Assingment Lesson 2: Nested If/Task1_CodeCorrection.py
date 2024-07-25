""" 1. Nested Decisions: The Adventure Game 🏰
Objective: To practice the use of nested if statements.

Task 1: Code Correction You are provided with a Python script 
that is supposed to guide a user through an adventure game, 
but it has some errors. Identify and fix them.

Buggy Code: """

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
