#Opens a file A in write mode
f1=open("fileA.txt",'w')
f1.write("My name is varishtaja\n")
f1.write("We are Piggy piggu family\n")
f1.write("I love god")
f1.close()

f2=open('fileB.txt','w')
f3=open("fileA.txt",'r')
for linesf1 in f3:
   print(linesf1)
   f2.write(linesf1)

f2.close()
f3.close()
