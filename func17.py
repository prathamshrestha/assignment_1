def check_string(input_string,input_char):
    check= lambda x:x[0].upper()==input_char.upper()
    if check(input_string):
        return f'Yes! The string starts with {input_char}'
    return f'No! The string doesn\'t start with {input_char}'

stringCheck=input('Enter any String:')
charCheck=input('Enter any Char to check:')
print(check_string(stringCheck,charCheck))