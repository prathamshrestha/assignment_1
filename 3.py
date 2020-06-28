astr=input('input a string ')

pstr=''
count=0

for i in astr:

    if count!=0:
        if ((i) == astr[0]):
        
            pstr=pstr+'$'    
        else:
            pstr=pstr+i
    else:
        pstr=astr[0]
    count+=1

print(pstr)
