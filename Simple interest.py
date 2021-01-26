P=int(input("Enter the principal amount:"))
T=int(input('Enter the time:'))
R=float(input('Enter the rate:'))

simple_interest=(P*T*R)/100
print(simple_interest)
amount=(P*(1+R/100)**T)
compound_interest=amount-P
print(compound_interest)

print(1200*(1+5.4/100)**2)
