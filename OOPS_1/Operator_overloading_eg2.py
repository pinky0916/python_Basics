class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        total=Student(m1,m2)
        return total
    def __gt__(self, other):
        a1=self.m1+self.m2
        b1=other.m1+other.m2
        if a1>b1:
            return True
        else:
            return False
    def __str__(self):
        return '{},{}'.format(self.m1,self.m2)

s1=Student(50,20)
s2=Student(25,50)

s3=s1+s2
print(s3.m1)
print(s3.m2)


print('************************')
if s1>s2:
    print("Student 1 is brillinat")
else:
    print("Student 2 is brilliant")

print('************************')
print(s1)
