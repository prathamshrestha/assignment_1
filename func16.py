def square_cube(input_list):
    list_square=[]
    list_cube=[]
    square = lambda x:x**2
    cube = lambda x:x**3
    for each in input_list:
        list_square.append(square(each))
        list_cube.append(cube(each))
    return f'square:{list_square}\ncube:{list_cube}'

print(square_cube([1,2,3,4,5,6,7,8]))