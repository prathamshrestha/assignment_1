def update_dict(input_dict):
    list_kv=[]
    for k,v in input_dict.items():
        list_kv.append((k,v))
    return list_kv

print(update_dict({1:10, 2:20, 3:30, 4:40, 5:50}))