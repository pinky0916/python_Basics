i=1;
while i<=5:
    print("#",end=" ")
    j=1
    while j<=5:
        print('#',end=" ")
        j=j+1
    i=i+1
    print(" ")
print("******************End of program 1********************")
for i in range(4):
    for j in range(4):
        print("#",end=" ")

    print()
print("******************End of program 2********************")
for i in range(4):
    for j in range(i+1):
        print('#',end=" ")
    print()
print("******************End of program 3********************")
for i in range(4):
    for j in range(4-i):
        print('#',end=" ")
    print()