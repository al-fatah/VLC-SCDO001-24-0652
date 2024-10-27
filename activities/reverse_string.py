def reverse_string(input_string):
    reversed_string = ""
    for i in range(1,len(input_string)+1):
        reversed_string += input_string[-i]
    return reversed_string

input_string = input("Enter a string: ")
print(f"The reversed string of '{input_string}' is {reverse_string(input_string)}")

