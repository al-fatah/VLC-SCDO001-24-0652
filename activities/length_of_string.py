def length_of_string(input_string):
    return len(input_string)
    

def length_of_string_with_loop(input_string):
    length = 0
    for i in input_string:
        length += 1
    return length

input_string = input("Enter a string: ")
print(f"The length of {input_string} using len() is {length_of_string(input_string)}", end="\n\n")
print(f"The length of {input_string} using loop is {length_of_string_with_loop(input_string)}", end="\n\n")