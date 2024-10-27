# *args 
# represents multiple positional arguments 

def add(*args):
    print(len(args))
    print(sum(args))
    # for i in args:
    #     print (i)
    print("--------------")


add(10,20)
add(10,20,20)
add(10,20,20,50,20)
add(10,20,20,50,20,10,20,20,50,10)



