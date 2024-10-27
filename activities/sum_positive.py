def sum_positive_numbers(input_list):
    sum = 0
    for i in input_list:
        if i > 0:
            sum += i
    return sum

list_one = [1,2,3,4,5,-1,-2,-3,-4,-5,0] 
list_two = [0,-1,-2,-3,-4,-5]
list_three = [0,1,-2]
print(f"The sum of the positive numbers in {list_one} is {sum_positive_numbers(list_one)}", end="\n\n")  #15 
print(f"The sum of the positive numbers in {list_two} is {sum_positive_numbers(list_two)}", end="\n\n")   #0
print(f"The sum of the positive numbers in {list_three} is {sum_positive_numbers(list_three)}", end="\n\n") #1  