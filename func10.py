def  find_even(input_list):
    list_even=[]
    check=lambda x: x%2==0
    for each in input_list:
        if check(each):
            list_even.append(each)
    return list_even


print(find_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))