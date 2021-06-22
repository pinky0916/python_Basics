#OFiles has 2 modes 1)character mode (text) and binary mode(images)
f1=open("image1 ",'rb')


f2=open('image2','wb')

for linesf1 in f1:
   print(linesf1)
   f2.write(linesf1)

