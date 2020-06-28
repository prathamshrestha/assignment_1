def slice_tuple(input_tuple):
    list_convert = list(input_tuple)
    sliced =list_convert[1:3]
    return(tuple(sliced))

print(slice_tuple(('BBA','BBS','CSIT','BE','BCOM')))