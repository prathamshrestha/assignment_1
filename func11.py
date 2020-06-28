def  add_num(input_number):
    sum_no= lambda x: x+15
    return sum_no(input_number)
def  mul_nums(num1,num2):
    mul= lambda x,y: x*y
    return mul(num1,num2)

print(add_num(3))
print(mul_nums(5,3))