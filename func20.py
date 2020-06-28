def intersect_array(arr1,arr2):
    intersect=[]
    check = lambda x: x in arr2
    for each in arr1:
        if check(each):
            intersect.append(each)
    return list(map(int,intersect))

arrayOne=input('Enter any Elemnts in array1 using space:').split()
arrayTwo=input('Enter any Elemnts in array2 using space:').split()
print(intersect_array(arrayOne,arrayTwo))