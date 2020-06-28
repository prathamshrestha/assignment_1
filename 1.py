astr=str(input('enter a string'))

count=0

for i in range(len(astr)):
    for j in range(len(astr)):
        if astr[i]==astr[j]:
            count+=1
    print(astr[i],' is repeated ',count,' times')
    count=0
