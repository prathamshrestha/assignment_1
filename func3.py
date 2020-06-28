from functools import reduce 
def mul_list(*args):
    return reduce(lambda a,b: a*b,args)

print(mul_list(8, 2, 3, -1, 7))