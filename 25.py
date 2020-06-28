def check_empty(input_list):
    for each in input_list:
        if each:
            return False
    return True


print(check_empty([{},{},{}]))
print(check_empty([{1,2},{},{}]))