alst=[]
n=int(input('enter no. of items in list'))
for i in range(n):
    a=int(input('enter tems to list'))
    alst.append(a)



res=alst[0]


for i in alst:
    if res<i:
        res=i
print('list is ',alst)


print('largest is ',res)