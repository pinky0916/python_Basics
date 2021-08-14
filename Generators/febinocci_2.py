

def febino(num):
  feb_list=[0,1]
  n1 = 0
  n2 = 1
  for i in range(0,num):

     sum=n1+n2
     feb_list.append(sum)
     n1=n2
     n2=sum
  print(feb_list)


num = int(input("How many febinocci series you want:"))
febino(num)