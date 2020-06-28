fstr=input('enter 1st string ')
sstr=input('enter 2nd string ')

fstr=list(fstr)
sstr=list(sstr)

for i in range(2):
    rstr=fstr[i]
    fstr[i]=sstr[i]
    sstr[i]=rstr

rstr=fstr+sstr

rstr=''.join(rstr)
print(rstr)