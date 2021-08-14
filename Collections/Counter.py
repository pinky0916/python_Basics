from collections import Counter
my_list=[1,1,1,1,2,2,2,3,3,3,4,4,4,5,6]
print(Counter(my_list))
print('************************************')
my_string='aaabbbbbzzzzzdddd'
print(Counter(my_string))

print('************************************')
sent='How are you Are you ok'
print(Counter(sent.lower().split()))

print('************************************')
#Saving the Counter value
sent='How are you Are you ok are ok are'
c=Counter(sent.lower().split())
#Most common function will return the most commonly used
print(c.most_common())

print(c.most_common(2))
#To convert it to a list, and gets the unique elements
print(list(c))


