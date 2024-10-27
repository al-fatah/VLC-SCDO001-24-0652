def is_palindrome(input_string):
    palindrome_string = ""
    for i in range(1,len(input_string)+1):
        palindrome_string += input_string[-i]
    return palindrome_string == input_string

print("Palindrome Checker",end="\n\n")
user_input = input("Enter a string: ").casefold()
print(f"{user_input} is a palindrome " if is_palindrome(user_input) else f"{user_input} is not a palindrome", end="\n\n")