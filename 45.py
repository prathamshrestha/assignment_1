def add_to_tuple(input_tuple,item):
    list_convert = list(input_tuple)
    if item in list_convert:
        return list_convert.index(item)
    return 'no item found in tuple'

findIndexOfItem=input('Enter string to be added')
print(add_to_tuple(('BBA','BBS','CSIT','BE','BCOM'),findIndexOfItem))