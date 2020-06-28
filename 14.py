def tagadd(tag,awrd):
    return "<%s>%s</%s>"%(tag,awrd,tag)

awrd=input('enter a word')
tag=input('enter a tag')
print(tagadd(tag,awrd))