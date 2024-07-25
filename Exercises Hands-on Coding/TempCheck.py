""" Write a Python program that:
1. Asks the user about the day's temperature in Celsius
2. Asks the user about the type of even they are attending(formal/casual)
3. Determines the outfit based on the above criteria
4. Displats the recommended outfit to the user. 

- If the temperature is below 15 degrees celsius and the even is "formal", suggest a "Warm formal suit"
- If the temperature is below 15 degrees celsius but the event is "casual", suggest a "Cozy sweater and jeans"
- If the temperature is above 15 degrees celsius and the event is "formal", suggest a "Light formal suit"
- For any other combination, suggest a "T-shirt and shorts"

** Hint:  Use nested if statements to determine the outfit based on the day's temperature and the type of event"""

temperature_check = int(input("What is the temperature of the day? (Celsius): "))
event_type = str(input("What type of even are you attending? (formal or casual): ").lower())

if temperature_check < 15:
    if event_type == "formal":
        print("Warm formal suit")
    elif event_type == "casual":
        print("Cozy sweater and jeans")
elif temperature_check > 15:
    if event_type == "formal": 
        print("Light formal suit")
    else:
        print("T-shirt and shorts")


