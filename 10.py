astr=input('enter a string ')
astr=list(astr)
for i in range(len(astr)):
    if i%2==0:
        astr[i]=''
astr=''.join(astr)
print(astr)