awrd=input('enter a sequence of word separated by only comma ')

words = [word for word in awrd.split(",")]
print(" ,".join(sorted(list(words))))

