alst=[]
res=1
n=int(input('enter no. of items in list'))
for i in range(n):
    a=int(input('enter tems to list'))
    alst.append(a)
    res=res*a
print('list is ',alst)


print('multiplies is ',res)