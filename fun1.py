def find_max(input_list):
    return sorted(input_list)[-1]

list_num=[]
for i in range(3):
    list_num.append(int(input(f'Enter number {i+1} :')))
print(find_max(list_num))