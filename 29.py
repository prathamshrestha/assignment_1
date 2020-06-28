def update_dict(dic1,dic2,dic3):
    d4={}
    for each in (dic1,dic2,dic3):
        d4.update(each)
    return d4

print(update_dict(dic1={1:10, 2:20}, dic2={3:30, 4:40},dic3={5:50,6:60}))