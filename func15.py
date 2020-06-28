def filter_list(input_list):
    filter_even = filter(lambda x:x%2==0,input_list)
    return list(filter_even)

print(filter_list([1,2,3,4,5,6,7,8]))