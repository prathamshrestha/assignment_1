def merge_dict(dic1,dic2):
    dict_merge={}
    for each in (dic1,dic2):
        dict_merge.update(each)
    return dict_merge

print(merge_dict(dic1={1:10, 2:20}, dic2={3:30, 4:40}))