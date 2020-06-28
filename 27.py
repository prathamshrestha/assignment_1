def replace_list(list_one,list_two):
    list_one.remove(list_one[-1])
    for each in list_two:
        list_one.append(each)
    return list_one

print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))