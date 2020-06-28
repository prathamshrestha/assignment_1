alst=[]
n=int(input('enter no. of items in list'))
for i in range(n):
    a=(input('enter items to list'))
    alst.append(a)

count=0

for i in alst:
    a=len(i)
    if a>2:
        if i[:1]==i[-1:]:
            count+=1
            

print('the number of strings where the string length is 2 or more and the first and last character are same is ',count)
