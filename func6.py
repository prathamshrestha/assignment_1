def check_range(start,end,check_value):
    if check_value in range(start,end+1):
        return f'Value {check_value} lies within the range'
    else:
        return f'Value {check_value} lies outside the range'

initial=int(input('Range Start'))
final=int(input('Range End'))
inputCheck=int(input('Enter to check number'))
print(check_range(initial,final,inputCheck))