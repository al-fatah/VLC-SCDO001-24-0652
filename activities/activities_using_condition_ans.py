# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# format the background
BLACK = "\033[40m"
RED_BG = "\033[41m"
GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
BLUE_BG = "\033[44m"
MAGENTA_BG = "\033[45m"
CYAN_BG = "\033[46m"
WHITE_BG = "\033[47m"

#format the text
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
ITALIC = "\033[3m"

'''
### Exercise 1: Grade Calculator
* Write a Python program to calculate a student's grade based on their score.
* The grading scale is as follows:
  * 90-100: A
  * 80-89: B
  * 70-79: C
  * 60-69: D
  * Below 60: F
* Prompt the user to enter their score and print the corresponding grade.
'''
print(WHITE_BG + GREEN + "🎓 Student Grade Calculator" + RESET)
raw_score = input(MAGENTA + "Enter the student's score: " + RESET)
if raw_score.isdigit():
    score = int(raw_score)
    if score >= 90 and score <= 100:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score < 60:
        grade = "F"    
    print(BLUE+f"The student's grade is: {grade}" +RESET)
    print(f"{BOLD +'-----Congratulations 🎉!-----' + RESET if grade in ('A','B')  else BOLD + '-----THE END-----' + RESET}")
else:
   print(RED + "⚠️ Warning: Invalid input" + RESET) 
print("")

'''
### Exercise 2: Leap Year Checker
* Write a Python program to determine whether a given year is a leap year.
* A year is a leap year if it is divisible by 4, but not divisible by 100, or if it is divisible by 400.
* Prompt the user to enter a year and print whether it's a leap year or not. 
'''

print(WHITE_BG + GREEN + "📅 Leap Year Checker" + RESET)
input_leap_year = input(MAGENTA + "Enter a year: " + RESET)
if input_leap_year.isdigit():
    leap_year = int(input_leap_year)
    if leap_year % 4 == 0 and (leap_year % 100 != 0 or leap_year % 400 == 0):
        print(BLUE + "📅 It is a leap year!" + RESET)
    else:
        print(RED + "❌ It is not a leap year." + RESET)
else:
    print(RED + "⚠️ Invalid input" + RESET)
print(BOLD + '-----THE END-----' + RESET)
print("")

'''
### Exercise 3: Vowel Checker
* Write a Python program to check whether a given character is a vowel or a consonant.
* Use a match-case statement to efficiently handle the vowel checking.
* Prompt the user to enter a character and print whether it's a vowel or a consonant.
'''
print(WHITE_BG + GREEN + "🔊 Vowel Checker" + RESET)    
input_char = input(MAGENTA + "Enter a character: " + RESET)
if input_char.isalpha() and len(input_char) == 1:
    char = input_char.lower()                   
    if char in 'aeiou':
        print(BLUE + "🔊 It's a vowel!" + RESET)
    else:
        print(RED + "🔇 It's a consonant." + RESET)
else:
    print(RED + "⚠️ Invalid input" + RESET)
print(BOLD + '-----THE END-----' + RESET)
print("")

'''
### Exercise 4: Number Classification
* Write a Python program to classify a number as positive, negative, 
zero, or one/negative one.
* Use a match-case statement to handle different number classifications.
* Prompt the user to enter a number and print its classification.
'''
print(WHITE_BG + GREEN + "🔢 Number Classification" + RESET)
num = int(input(MAGENTA + "Enter a number: " + RESET))
if num > 0 and num not in (-1, 1):
    print(BLUE + "🔢 It's a positive number!" + RESET)
elif num < 0 and num not in (-1, 1):
    print(BLUE + "🔢 It's a negative number!" + RESET)
else:
    match num:
        case 0:
            print(BLUE + "0️⃣ It's zero!" + RESET)
        case 1:
            print(BLUE + "1️⃣ It's one!" + RESET)
        case -1:
            print(BLUE + "🔢 It's negative one!" + RESET)
        case _:
            print(RED + "⚠️ Invalid input" + RESET)
print(BOLD + '-----THE END-----' + RESET)
print("")

'''
### Exercise 5: Simple Calculator
* Write a Python program to perform basic arithmetic operations (addition, subtraction, multiplication, and division).
* Use a match-case statement to handle different operators.
* Prompt the user to enter two numbers and an operator, and then perform the calculation.
* Handle the case of division by zero.
'''
print(WHITE_BG + GREEN + "🧮 Simple Calculator" + RESET)
num_one = float(input("Enter a number: "))
num_two = float(input("Enter a second number: "))
operator = input("Select an operation ([a]dd [s]ubstract [m]ultiply [d]ivide): ").lower()
match operator:
    case "a":
        print(BLUE + f"Result: {num_one + num_two}" + RESET)
    case "s":
        print(BLUE + f"Result: {abs(num_one - num_two)}" + RESET)
    case "m":
        print(BLUE + f"Result: {num_one * num_two}" + RESET)
    case "d":
        print(BOLD +"num_two will be divided by num_one" + RESET)
        print( BOLD +RED + "❌ Not divisible by 0" + RESET if num_two == 0 else BLUE + f"Result: {num_one / num_two :,.2f}" + RESET)
    case _:
        print(RED + "⚠️ Invalid input" + RESET)
print(BOLD + '-----THE END-----' + RESET)
print("")

'''
### Exercise 6: Password Strength Checker:
* Write a program that takes a password as input and checks the strength based on length:
* Less than 6 characters: Weak.
* Between 6 and 10 characters: Medium.
* More than 10 characters: Strong.
'''
print(WHITE_BG + GREEN + "🔑 Password Strength Checker" + RESET)
password_length = len(input(MAGENTA + "Enter a password: " + RESET))
if password_length < 6:
    print(RED + "⚠️ Weak password" + RESET)
elif password_length >= 6 and password_length <= 10:
    print(YELLOW + "⚠️ Medium password" + RESET)
else:
    print(GREEN + "🔒 Strong password" + RESET)
print(BOLD + '-----THE END-----' + RESET)
print("")

'''
### Exercise 7: Traffic Light Simulation:
* Write a program that simulates a traffic light using a match expression. 
* Ask the user to enter a color (Red, Yellow, or Green) 
* print what they should do (e.g., "Stop", "Slow down", or "Go").
'''
print(WHITE_BG + GREEN + "🚦 Traffic Light Simulation" + RESET)
light_color = input(MAGENTA + "Enter a color ([R]ed, [Y]ellow, or [G]reen): " + RESET).lower()
match light_color:
    case "r":
        print(RED + "🔴 Stop"  + RESET)
    case "y":
        print(YELLOW + "🟡 Slow down"  + RESET)
    case "g":
        print(GREEN + "🟢 Go" + RESET)
    case _:
        print(RED + "⚠️ Invalid input" + RESET)
print(BOLD + '-----THE END-----' + RESET)
print("")

'''
### Exercise 8: Season Finder:
* Create a program that takes a month (as an integer) from the user 
* use a match expression to print the season (Winter, Spring, Summer, Autumn) based on the month.
'''
print(WHITE_BG + GREEN + "🌞 Season Finder" + RESET)
input_month = input(MAGENTA + "Enter a month (1-12): " + RESET)
if input_month.isdigit():
    month = abs(int(input_month))
    match month:
        case 1 | 2 | 12:
            print(BLUE + "❄️ Winter" + RESET)
        case 3 | 4 | 5:
            print(GREEN + "🌱 Spring" + RESET)
        case 6 | 7 | 8:
            print(YELLOW + "☀️ Summer" + RESET)
        case 9 | 10 | 11:
            print(MAGENTA + "🍂 Autumn" + RESET)
        case _:
            print(RED + "❌ Invalid input" + RESET)
else:
    print(RED + "⚠️ Invalid input" + RESET)
print(BOLD + '-----THE END-----' + RESET)
print("")


'''
### Exercise 9: Mix of if and match
* Write a program that asks the user to choose between a 
temperature unit (Celsius or Fahrenheit) using a match expression. 
* Then, based on the unit * chosen, use if statements to determine whether the temperature is cold, moderate, or hot:
* Celsius:
-----------
* Below 10°C: Cold
* 10°C to 25°C: Moderate
* Above 25°C: Hot

* Fahrenheit:
-----------
* Below 50°F: Cold
* 50°F to 77°F: Moderate
* Above 77°F: Hot
'''
print(WHITE_BG + GREEN + "🌡️ Temperature Checker" + RESET)
temp_unit = input(MAGENTA + "Enter a temperature unit ([C]elsius or [F]ahrenheit): " + RESET).lower()
match temp_unit:
    case "c":
        temp = float(input(MAGENTA + "Enter the temperature in Celsius: " + RESET))
        if temp < 10:
            print(BLUE + "❄️ Cold" + RESET)
        elif 10 <= temp <= 25:
            print(GREEN + "🌞 Moderate" + RESET)
        elif temp > 25:
            print(RED + "🔥 Hot" + RESET)
    case "f":
        temp = float(input(MAGENTA + "Enter the temperature in Fahrenheit: " + RESET))
        if temp < 50:
            print(BLUE + "❄️ Cold" + RESET)
        elif 50 <= temp <= 77:
            print(GREEN + "🌞 Moderate" + RESET)
        elif temp > 77:
            print(RED + "🔥 Hot" + RESET)
    case _:
        print(RED + "⚠️ Invalid input" + RESET)
print(BOLD + '-----THE END-----' + RESET)
print("")

'''
### Exercise 10: Age check
* write a program that accepts the users age 
* verify if he/she is eligible to vote (age above 18 is eligible for voting)
'''
print(WHITE_BG + GREEN + "👴 Age Checker" + RESET)
input_age = input(MAGENTA + "Enter your age: " + RESET)
if input_age.isdigit():
    age = abs(int(input_age))
    print(BLUE + "👴 You are eligible to vote!"+ RESET if age >= 18 else RED + "❌ You are not eligible to vote." + RESET)
else:
    print(RED + "⚠️ Invalid input" + RESET)
print(BOLD + '-----THE END-----' + RESET)
print("")

