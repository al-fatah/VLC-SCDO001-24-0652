#using sum()
def sum_of_tuple(input_tuple):
    return sum(input_tuple)

tuple_one = (1,2,3,4,5)
tuple_two = (1,2,3,4,5,6,7,8,9,10)
print(f"The sum of {tuple_one} is {sum_of_tuple(tuple_one)}", end="\n\n")#15
print(f"The sum of {tuple_two} is {sum_of_tuple(tuple_two)}", end="\n\n")#55

#with loop
def sum_of_tuple_with_loop(input_tuple):
    sum = 0
    for i in input_tuple:
        sum += i
    return sum

print(f"The sum of {tuple_one} with loop is {sum_of_tuple_with_loop(tuple_one)}", end="\n\n")#15
print(f"The sum of {tuple_two} with loop is {sum_of_tuple_with_loop(tuple_two)}", end="\n\n")#55