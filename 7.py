
res=''
def longest(word):
    
    res=word.split()
    long=len(res[0])
    for i in res:
        if long<len(i):
            long=len(i)
    return long


astr=input('enter list of words ')
print(longest(astr))
