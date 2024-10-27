
# def print_red(s):
#     print("\033[31m"+ s + "\033[0m")

# # use lambda
print_red = lambda s: f'"\033[31m {s} \033[0m"'  # noqa: E731
add = lambda a,b: a+b  # noqa: E731


print(print_red("this is in red"))