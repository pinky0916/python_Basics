#Withouse pass the below code will throw error as for loop expecting some statements:
a='sammy'
for i in a:
    pass
print("Print me ")
print('*************************')
#Continue
b='SNNOBYTY'
for j in b:
    if j=='N':
        continue
    print(j)
print('*************************')
#Break
for j in b:
    if j=='N':
        break
    print(j)
print('Loop exited')
print('*************************')
#While with Break
x=0
while x<5:
    if x==2:
        break
    print(x)
    x=x+1
print('Loop exited')