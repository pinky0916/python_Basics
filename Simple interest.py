P=int(input("Enter the principal amount:"))
T=int(input('Enter the time:'))
R=float(input('Enter the rate:'))

simple_interest=(P*T*R)/100
print(f'simple_interest is :{simple_interest}')
amount=(P*(1+R/100)**T)
print(f'compound interest is :{amount-P}')

#using pow()  instead of **
amount1=P*(pow((1+R/100),T))
print(f'Amount using pow function is :{amount1}')
print(f'compound interest 2 is :{amount1-P}')

print(1200*(1+5.4/100)**2)
