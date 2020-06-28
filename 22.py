lst=[]
n=int(input('enter no. of elements in list you want to put '))
for i in range(n):
    a=int(input('enter a no. to list ' ))
    lst.append(a)
print('list is ',lst)
alst=[]
for i in lst:
    for j in lst:
        if j not in alst:
            alst.append(j)
            

print('the final list is ',alst)