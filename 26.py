def string_input(input_list,insert_str):
    for i in range(len(input_list)):
        input_list[i]=insert_str + str(input_list[i])
    return input_list

print(string_input([1,2,3,4],'emp'))