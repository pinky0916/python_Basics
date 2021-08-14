from collections import defaultdict
d={'a':10,'b':20,'c':30}

print(d['c'])
#print(d['WRONG'])  #this will throw error since it doenst exist

#defining the default dictionary
d=defaultdict(lambda:0)
print(d['WRONG'])
