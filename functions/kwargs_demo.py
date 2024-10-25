# **kwargs
# keyword args
# represents multiple key value pairs

def print_info(**kwargs):
    for k,v in kwargs.items():
        print(k,v)


print_info(name= "Alice", age= 35, city="NY")