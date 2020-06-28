from functools import reduce
def mul_dict(input_dict):
    return reduce(lambda a,b:a*b ,input_dict.values())

print(mul_dict({1:10, 2:20, 3:30, 4:40, 5:50}))