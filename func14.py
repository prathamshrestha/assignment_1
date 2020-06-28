def sort_dict(input_dict):
    check = lambda x:sorted(x)
    return dict(check(input_dict.items()))

print(sort_dict({2:20,1:10,4:40,5:50,3:30}))