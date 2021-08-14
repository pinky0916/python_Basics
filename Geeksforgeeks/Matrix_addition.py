
print("Method#1")
A = [[1,2],
     [3,4]]

B = [[9,8],
     [1,2]]

result=[list(map(sum,zip(*t))) for t in zip(A,B)]
print(list(result))


print('**************************************************')
print("Method#2")
x=[[1,2,3,4],
   [4,5,6,5],
   [7,8,9,10]]
y=[[9,8,7,1],
   [6,5,4,1],
   [3,2,1,1]]
z=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]

for i in range(len(x)):
    for j in range(len(x[i])):
        z[i][j]=x[i][j]+y[i][j]

#print(z)
for i in z:
    print(i)

