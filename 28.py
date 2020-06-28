def add_key(input_key,input_value,final_dict):
    final_dict[input_key]=input_value
    return final_dict

key=int(input("add integer key"))
value=int(input("add integer value"))


key=input("add integer key")
value=input("add integer value")
print(add_key(key,value,{0: 10, 1: 20}))