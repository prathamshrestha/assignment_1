astr=input('enter a string ')
n=int(input('enter a index to remove it '))
astr=list(astr)
astr.pop(n-1)
astr=''.join(astr)

print(astr)