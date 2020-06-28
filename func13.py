def sort_tuple(input_tuple):
    check = lambda x:sorted(x)
    return tuple(check(input_tuple))

print(sort_tuple((6,2,3,7,8,1,4,5)))