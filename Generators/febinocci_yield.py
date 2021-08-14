def feb_yield(n):
    n1=0
    n2=1
    for i in range(0,n):
        yield n1
        n1,n2=n2,n1+n2

for num in feb_yield(10):
    print(num)