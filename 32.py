def create_dict(n):
    return {each:each**2 for each in range(1,n+1)}

takeInput=int(input("Input range"))
print(create_dict(takeInput))