num=11
# prime_flag = True
for i in range(2, num):
    if num % i == 0:
        prime_flag = False
        break
else:
    prime_flag = True

if prime_flag:
    print("Prime")
else:
    print("Not prime")

