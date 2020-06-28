def add_to_tuple(input_tuple,item):
    list_convert = list(input_tuple)
    if item in list_convert:
        list_convert.remove(item)
        return(tuple(list_convert))
    return 'no item found in tuple'

itemToRemove=input('Enter string to be added')
print(add_to_tuple(('BBA','BBS','CSIT','BE','BCOM'),itemToRemove))