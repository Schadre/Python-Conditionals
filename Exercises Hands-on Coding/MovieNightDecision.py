""" You are developing a feature for a movie streaming platform that suggests
a movie genre to users based on their current mood and the day's weather.
The platform has the following recommendation criteria:

- If the user is feeling "happy" and the weather is "sunny" recommend a "Comedy".
- If the user is feeling "happy, but the weather is not "sunny", recommend a "Romantic" movive.
- If the user is feeling "sad", recommend a "Drama".
- For any other mood, recommend an "Adventure" movie.

Write a Python program that:
1. Ask the user about their current mood(happy/sad/adventurous).
2. Ask the user about the day's weather(sunny/rainy).
3. Determines the movie genre based on the above criteria.
4. Displays the recommended movie genre to the user.

** Hint: Use nested "if" statments to determine the movie genre based on the user's mood and the day's weather. """

current_mood = str(input("How are you feeling today?(happy/sad/adventurous) ").lower())
weather = str(input("What is the weather like?(sunny/rainy) ").lower())

if current_mood == "happy":
    if weather == "sunny":
        print("Comedy")
    elif weather == "rainy":
        print("Romantic")
elif current_mood == "sad":
    print("Drama")
else:
    print("Adventure")
