from functools import reduce
def fact(input_no):
    if input_no > 0:
        return reduce(lambda a,b: a*b,range(1,input_no+1))
    return 'Pass Positive Number'

print(fact(int(input("Enter any No."))))