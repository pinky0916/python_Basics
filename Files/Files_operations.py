f1=open("File1.txt",'r')
print(f1.read())
print("***********")
#if we dont give seek pointer will be at the end of the text, so need to reset if need to read again
f1.seek(0)
print(f1.read())
print("***********")
#To return as list
f1.seek(0)
print(f1.readlines())