'''
1. Personal Information Formatter
Prompt the user for their 
first name, 
last name, 
age, 
and favorite color.
Print a formatted sentence, like: 
"Hello, [first name] [last name]! 
You are [age] years old, and your favorite color is [color]."
'''

first_name = input("What is your first name?")
last_name = input("What is your last name?")
age = input("What is your age name?")
fav_color = input("What is your favourtie color?")
print(f"Hello, {first_name.title()} {last_name.title()}! You are {age} years old, and your favorite color is {fav_color}.")

'''
2. Simple Math Operations
Ask the user for two numbers and store them as integers.
Perform and print the results for addition, subtraction, multiplication, and division of these numbers.
Display the results with descriptive messages, e.g., "The sum is: [result]."

'''
number_one = int(input("Input any integer"))
number_two = int(input("Input another integer"))
print(f"The addition of the two numbers gives {number_one + number_two}")
print(f"The subtraction of the two numbers gives {number_one - number_two}")
print(f"The multiplication of the two numbers gives {number_one * number_two}")
print(f"The division of the two numbers gives {round(number_one / number_two)}")

'''
3. String Manipulation
Prompt the user to enter a word.
Print the word in uppercase, lowercase, and the number of characters in it.
Also, print the first and last character of the word.

'''

word = input("Enter a word")
print(f"{word.upper() = }")
print(f"{word.lower() = }")
print(f"{len(word) = }")
print(f"The first character is {word[0]} and the last character is {word[1]}")

'''
4. Area and Perimeter Calculator
Ask the user for the length and width of a rectangle.
Calculate and print the area (length × width) and the perimeter (2 × (length + width)).

'''

length = float(input("What is the length of your rectangle?"))
width = float(input("What is the width of your rectangle?"))
print(f"The area of your rectangle is {length * width}")
print(f"The perimeter of your rectangle is {2*(length + width)}")

'''
5. Birthday Year Calculator
Ask the user for their current age.
Calculate and print the year they were born based on the current year (use a fixed year, like 2024, for simplicity).

'''

birth_year = int(input("What is your birth year?"))
print(f"Your birth year is {birth_year}. The year is 2024. You are {2024-birth_year} years old")

'''
6. Distance Converter
Prompt the user for a distance in kilometers.
Convert it to miles (1 km ≈ 0.621371 miles) and display the result.

'''

distance = float(input("Provide a distance in km"))
print(f"The distance of {distance}km is {round(distance*0.621371,2)}miles")

'''
7. Grocery Bill
Ask the user for prices of three grocery items.
Calculate the total and average cost of these items.
Print the results with a formatted message.
'''

egg = float(input("What is the price of eggs?"))
milk = float(input("What is the price of milk?"))
bread = float(input("What is the price of bread?"))
print(f"The total price of your groceries is ${egg+milk+bread:.2f} and the average price is ${(egg+milk+bread)/3:.2f}")