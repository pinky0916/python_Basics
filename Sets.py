#sets are unordered collection of unique objects, values should be unique
myset=set()
myset.add(2)
myset.add(2) # this will not work
print(myset)

#Casting a list to a set
my_list=[1,2,3,2,2,3,4]
my_set2=set(my_list)
print(my_set2)