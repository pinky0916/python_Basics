def create_cubes(n):
    result=[]
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))

for x in create_cubes(10):
    print(x)

print('*******************************')
def create_cubes(n):


    for x in range(n):
        yield x**3
    
for x in create_cubes(10):
    print(x)