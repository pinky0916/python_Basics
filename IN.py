#To check if a value is avaialble in a list or string
a='X' in ['X','Y','Z']
print(a)
print('*******1*************')

a='A' in ['a','b','c']
print(a)
print('*******2************')
#to check in string
c= 'I' in ("I love Newyork")
print(c)
print('********3***********')
#to check in dictionary- it will check for keys,not values
d={'k1':1,'k2':2,'k3':3}
e='k5' in d
print(e)
print('*******4************')
#to check in dictionary- it will check for values
d1={'k1':5,'k2':4,'k3':10}
e1=10 in d1.values()
e2=100 in d1.values()
print(e1)
print(e2)
print('********5***********')
#to check in dictionary- it will check for keys
d1={'k1':5,'k2':4,'k3':10}
e1='k3' in d1.keys()
e2='k5' in d1.keys()
print(e1)
print(e2)