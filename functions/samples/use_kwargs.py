def create_dict(**kwargs):
    my_dict= {}
    for k,v in kwargs.items():
        my_dict[k] = v
    return my_dict

d = create_dict(name="Alex",age=30,city="Singapore")

print(d)

a = create_dict(a="a",b='b',c='c', d='d')
print(a)

