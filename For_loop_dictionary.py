d={'k1':1,'k2':2,'k3':3}
#By default dictionaries return keys
for a in d:
    print(a)
print('******************************************')
#to print as key ,value pairs
for  a in d.items():
    print(a)
print('******************************************')
#to access keys and values separately
for x,y in d.items():
    print(f'Keys are :{x}')
    print(f'Values are :{y}')
print('******************************************')
#to get only values
for y in d.values():
    print("The values are {}".format(y))

