#it provides the index position with the elements as tuple, llar to tuple unpacking:
word='ABCDE'
for x in enumerate(word):
    print(x)
print('*******************************')
for x,y in enumerate(word):
    print(x)
    print(y)
    print('\n')