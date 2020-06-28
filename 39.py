def unpack_tuple(input_tuple):
    a,b,c,d,e=tuple(each for each in input_tuple)
    return f'{a} {b} {c} {d} {e}'

print(unpack_tuple(('BBA','BBS','CSIT','BE','BCOM')))