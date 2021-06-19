#Dictionaries are unordered objects with key value pairs,can hold of mixed object types
#easy retriveable by keys ,not by index,Unordered,cannot sort
#List-retrievable by index,ordered,sorting is possible,indexing and slicing,
#Key should always be string

d={'key1':'value1','key2':'value2'}
print(d['key1'])


d1={'k1':123,'k2':[0,1,2],'k3':{'insidekey':100}}
print(d1['k3']['insidekey'])

d2={'k1':['a','b','c']}
print(d2['k1'][2].upper())

#Insert new values at the end .
d3={'k1':1,'k2':2,'k3':3}
d3['k4']=4
print(d3)

#to change the key or the value
d3['k2']='Changed value'
print(d3)

#to change the key:

#to retrive all the keys
print(d3.keys())
#to retrieve the values
print(d3.values())
#to retrieve as pairings
print(d3.items())
