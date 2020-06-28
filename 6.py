astr=input('enter a satement ')

len1=len(astr)
astr=list(astr)

for i in range(len1-3):
    sub1=astr[i:i+3]
    sub1=''.join(sub1)
    if sub1=='not':
        j=i
        
    
        for j in range(len1-3):
            sub2=astr[j:j+4]
            sub2=''.join(sub2)
            if sub2=='poor':
                astr[i:j+4]='good'

astr=''.join(astr)

print(astr)
