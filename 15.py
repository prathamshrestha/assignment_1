def ins(param,word):
    res=param[:2]+word+param[2:]
    return res

str1=input('enter 1st string ')
str2=input('enter 2nd string ')

print(ins(str1,str2))