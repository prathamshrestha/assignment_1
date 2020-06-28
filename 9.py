astr=input('enter a string ')
astr=list(astr)
rep=astr[0]
astr[0]=astr[-1]
astr[-1]=rep
astr=''.join(astr)
print(astr)