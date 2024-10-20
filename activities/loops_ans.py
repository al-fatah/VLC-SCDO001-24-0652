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
### 1. **Sum of Numbers**
Write a Python program that asks the user to input a number `n` and then calculates the sum of all numbers from 1 to `n` 
using a loop.
'''
print(WHITE_BG + GREEN + '➕' + " Sum of Numbers" + RESET )
raw_number = input("Enter a number: ")

if raw_number.isdigit():
    number=int(raw_number)
    sum = 0
    for i in range(1,number+1):
        sum += i
    print(BLUE + f"The sum of digits from 1 to {number} is {sum}" + RESET, end="\n\n")
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n") 

'''
### 2. **Factorial Calculation**
Write a program that calculates the factorial of a given number using a loop.
'''
print(WHITE_BG + GREEN + '❗' + " Factorial Calculations" + RESET )
raw_number = input("Enter a number: ")
if raw_number.isdigit():
    number=int(raw_number)
    total = 1
    for i in range(1,number+1):
        total *=i
    print(BLUE + f"The factorial of {number} is {total}" + RESET, end="\n\n")
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n") 


'''
### 3. **Fibonacci Sequence**
Create a Python program that prints the first `n` numbers of the Fibonacci sequence, where `n` is input by the user.
'''
print(WHITE_BG + GREEN + '🦪' + " Fibonacci Sequence Calculations" + RESET )
raw_number = input("Enter a number: ")
if raw_number.isdigit():
    number=int(raw_number)
    number_one = 0
    number_two = 1
    next_num = 0
    for i in range(1,number+1):
        print(number_one, end="\n\n" if i == number else ", ")    
        next_num = number_one + number_two
        number_one = number_two
        number_two = next_num
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n") 

'''
### 4. **Multiplication Table**
Write a program that prints the multiplication table for a given number using a loop.
'''
print(WHITE_BG + GREEN + '✖' + " Multiplication Table" + RESET )
raw_number = input("Enter a number: ")
if raw_number.isdigit():
    number=int(raw_number)
    print("Multiplication of {number}")
    print('-'*40)
    for i in range (1,11):
        print(BLUE + f"{number} x {i} = {number*i}" + RESET)
    print('-'*40, end='\n\n')
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n") 


'''
### 5. **Check Prime Number**
Write a Python program that checks whether a number entered by the user is a prime number using a loop.
'''
print(WHITE_BG + '𝐏𝐫𝓲𝓂𝑒 🔢' + RESET )
raw_number = input("Enter a number: ")
if raw_number.isdigit():
    number=int(raw_number)
    is_prime = True
    for i in range (2,number):
        if number % i == 0:
            is_prime = False
            break
    print(BLUE + f"{number} is a prime number" if is_prime else f"{number} is not a prime number" + RESET, end="\n\n")  
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n") 

'''
### 6. **Reverse a String**
Write a Python program that takes a string as input and 
prints the string in reverse using a loop.
'''
print(WHITE_BG + GREEN + '🔄' + " Reverse a String" + RESET )
input_string = input("Enter a string: ")
reverse_string = ""
for i in range(len(input_string)-1,-1,-1):
    reverse_string += input_string[i]
print(BLUE + f"The reverse of {input_string} is {reverse_string}" + RESET, end="\n\n")

'''
### 7. **Count Vowels**
Write a Python program that counts the number of vowels in a given string using a loop.
'''
print(WHITE_BG + GREEN + '🔊' + " Count Vowels" + RESET )
input_string = input("Enter a string: ").casefold()
vowel_count = 0
for i in input_string:
    if i.lower() in "aeiou":
        vowel_count += 1
print(BLUE + f"The number of vowels in {input_string} is {vowel_count}" + RESET, end="\n\n")

'''
### 8. **Print a Pattern**
Write a program that prints the following pattern using nested loops:
```
*
**
***
****
*****
```
'''
print(WHITE_BG + GREEN + '﹌﹌﹌﹌﹌' + " Print a Pattern " + '﹌﹌﹌﹌﹌' + RESET )
for i in range(1,6):
    print('*'*i)
print('', end='\n\n')
'''
### 9. **Sum of Even Numbers**
Write a Python program to calculate the sum of all even numbers 
between 1 and `n` using a loop.
'''
print(WHITE_BG + GREEN + '➕' + " Sum of Even Numbers" + RESET )
raw_number = input("Enter a number: ")
if raw_number.isdigit():
    number=int(raw_number)
    sum = 0
    for i in range(2,number+1,2):
        sum += i
    print(BLUE + f"The sum of even numbers from 1 to {number} is {sum}" + RESET, end="\n\n")
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n") 
'''
### 9. **Sum of Even Numbers**
Write a Python program to calculate the sum of all even numbers 
between 1 and `n` using a loop.
'''
print(WHITE_BG + GREEN + 'ه = ∑∞ⁿ⁼⁰ ¹ₙ' + " Sum of Even Numbers" + RESET )
raw_number = input("Enter a number: ")
if raw_number.isdigit():
    number=int(raw_number)
    sum = 0
    for i in range(2,number+1):
        if i%2 == 0:
            sum += i
    print(BLUE + f"The sum of even numbers from 1 to {number} is {sum}" + RESET, end="\n\n")
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n") 

'''
### 10. **Number of Digits**
Write a Python program to count the number of digits in an integer entered by the user.
'''
print(WHITE_BG + GREEN + '🔢' + " Number of Digits" + RESET )
number = input("Enter a number: ")
if number.isdigit():
    print(BLUE + f"The number of digits in {number} is {len(number)}" + RESET, end="\n\n")
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n") 

'''
### 11. **Find the Largest Number**
Write a Python program that takes `n` numbers as input and finds the largest number among them using a loop.
'''
print(WHITE_BG + GREEN + '🔢' + " Find the Largest Number" + RESET )
raw_count_number = input("How many numbers would you like to enter? : ")
if raw_count_number.isdigit():
    count_number = int(raw_count_number)
    i = 0
    numbers = []
    while i < count_number:
        raw_number = input(f"Enter number {i+1}: ")
        number = int(raw_number) if raw_number.isdigit() else print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n")
        numbers.append(number)
        i += 1
    print(BLUE + f"The largest number in {numbers} is {max(numbers)}" + RESET, end="\n\n")              
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n")


''' 
### 12. **Guess the Number**
Create a number guessing game where the user has to guess a number between 1 and 100. Use a loop to keep asking the user until they guess correctly.
'''
magic_number = '56'
print(WHITE_BG + GREEN + '❓ ' + " Guess the Number" + RESET )
user_input = input("What is the magic number between 1 and 100? ")
counter = 0
while counter <10:
    if user_input == magic_number:
        print(BLUE + '🎉🥳🎊🎁'+f"Congratulations! You guessed the magic number {magic_number}" + RESET, end="\n\n")
        break
    else:
        print(f"You have {10-counter} tries left")
        user_input = input("Try again: ")
        counter += 1
        if counter ==10:
            print(RED + '🚫' + " Warning: You have used all your tries" + RESET, end="\n\n")
            break

'''
### 13. **Palindromic Number**
Write a Python program that checks whether a given number is a palindrome (same when read forwards and backwards) using a loop.
'''
print(WHITE_BG + GREEN + '1️⃣5️⃣1️⃣' + " Palindromic Number" + RESET )
user_input = input("Enter a number: ")
palindromic_number = ""
for i in range(1,len(user_input)+1):
    palindromic_number += user_input[-i]
print(BLUE + f"{user_input} is a palindromic number" if palindromic_number == user_input else f"{user_input} is not a palindromic number" + RESET, end="\n\n")

'''
### 14. **Sum of Digits**
Write a Python program that calculates the sum of the digits of a given integer using a loop.
'''
print(WHITE_BG + GREEN + '➕' + " Sum of Digits" + RESET )
user_input = input("Enter a number: ")
if user_input.isdigit():
    sum_of_digits = 0
    for i in user_input:
        sum_of_digits += int(i)
    print(BLUE + f"The sum of digits of {user_input} is {sum_of_digits}" + RESET, end="\n\n")
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n")

'''
### 15. **Find the GCD**
Write a Python program to find the greatest common divisor (GCD) of two numbers using a loop.
'''
print(WHITE_BG + GREEN + '➗' + " Greatest Common Divisor" + RESET )
user_input_one = input("Enter a number: ")
user_input_two = input("Enter another number: ")
if user_input_one.isdigit() and user_input_two.isdigit():
    number_one = int(user_input_one)
    number_two = int(user_input_two)
    gcd = 1
    for i in range(2,min(number_one,number_two)+1):
        if number_one % i == 0 and number_two % i == 0:
            gcd = i
    print(BLUE + f"The greatest common divisor of {number_one} and {number_two} is {gcd}" + RESET, end="\n\n")
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n")

'''
### 16. **Find the LCM**
Write a Python program that calculates the least common multiple (LCM) of two numbers using a loop.
'''
print(WHITE_BG + GREEN + '➗' + " Greatest Common Multiple" + RESET )
user_input_one = input("Enter a number: ")
user_input_two = input("Enter another number: ")
if user_input_one.isdigit() and user_input_two.isdigit():
    number_one = int(user_input_one)
    number_two = int(user_input_two)
    gcd = 1
    for i in range(2,min(number_one,number_two)+1):
        if number_one % i == 0 and number_two % i == 0:
            gcd = i
    lcm = number_one * number_two / gcd
    print(BLUE + f"The least common multiple of {number_one} and {number_two} is {round(lcm)}" + RESET, end="\n\n")
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n")

'''
### 17. **Pattern of Numbers**
Write a Python program to print the following number pattern using nested loops:
```
1
12
123
1234
12345
```
'''
print(WHITE_BG + GREEN + '﹌﹌﹌﹌﹌' + " Print a Pattern " + '﹌﹌﹌﹌﹌' + RESET )
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

'''
### 18. **Remove Duplicates from a List**
Write a Python program that removes all duplicates from a list using a loop.
'''
print(WHITE_BG + GREEN + '👯' + " Remove Duplicates from a List" + RESET )
list_of_duplicates = [1,2,2,"orange","orange","apple",3,4,4]
unique_list = []
for i in list_of_duplicates:
    if i not in unique_list:
        unique_list.append(i)
print(BLUE + f"The list without duplicates is {unique_list}" + RESET, end="\n\n")

'''
### 19. **Sum of Series**
Write a Python program that calculates the sum of the following series up to `n` terms using a loop:
```
S = 1 + 1/2 + 1/3 + ... + 1/n
```
'''
print(WHITE_BG + GREEN + '➕' + " Sum of Series" + RESET )
raw_number = input("Enter a number: ")
if raw_number.isdigit():
    number = int(raw_number)
    sum_of_series = 0
    for i in range(1,number+1):
        sum_of_series += 1/i
    print(BLUE + f"The sum of series is {sum_of_series:.2f}" + RESET, end="\n\n")
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n")

'''
### 20. **Find the Smallest Number**
Write a Python program that takes `n` numbers as input and finds the smallest number among them using a loop.
'''
print(WHITE_BG + GREEN + '🔢' + " Find the Smallest Number" + RESET )
raw_count_number = input("How many numbers would you like to enter? : ")
if raw_count_number.isdigit():
    count_number = int(raw_count_number)
    i = 0
    numbers = []
    while i < count_number:
        raw_number = input(f"Enter number {i+1}: ")
        if raw_number.isdigit():
            number = int(raw_number)
            numbers.append(number)
            i += 1
        else: 
            print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n")
    print(BLUE + f"The smallest number in {numbers} is {min(numbers)}" + RESET, end="\n\n")       
else:
    print(RED + '🚫' + " Warning: Invalid input" + RESET, end="\n\n")




