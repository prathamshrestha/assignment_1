astr=input('enter a string ')
len1=len(astr)
if len1>=3 :
    if astr[-3:] == 'ing':
        astr=astr+'ly'
    else:
        astr=astr+'ing'

print(astr)