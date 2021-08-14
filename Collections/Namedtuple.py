from collections import namedtuple
#constructing a named tuple
Dog=namedtuple('Dog',['age','breed','name'])

#Create an object of this named tuuple:
sammy=Dog(age=5,breed='Husky',name='Coffee')
print(type(sammy))
print(sammy.age,sammy.name,sammy[0])
