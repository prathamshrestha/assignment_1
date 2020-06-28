def check_prime(input_number):
    if input_number <0:
        return f'Enter Positive'
    if  input_number==0 and input_number==1:
        return f'Neither Prime Nor Composite'
    check = lambda x: (x % i != 0  for i in range(2,input_number))
    if all(check(input_number)):
        return f'Prime'
    return 'Composite'

print(check_prime(int(input("Enter any No."))))