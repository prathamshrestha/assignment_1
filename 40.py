def add_to_tuple(input_tuple,item):
    list_convert = list(input_tuple)
    list_convert.append(item)
    return(tuple(list_convert))

itemtoEnter=input('Enter string to be added')
print(add_to_tuple(('BBA','BBS','CSIT','BE','BCOM'),itemtoEnter))