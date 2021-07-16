def user_input():
    print('Hi')
    guess_numb=5
    while (guess_numb not in range(0,3)):
      guess_numb=int(input("Enter a number 0,1,2:"))
    return (guess_numb)
def generate_random(list1):
    from random import shuffle
    shuffle(list1)
    print(list1)
    return list1
def check_match(shuffled_list,user_guess):
    if shuffled_list[user_guess]=='0':
        print("wow both matches")
    else:
        print('Wrong guess')




user_guess=user_input()
print(f'User has guessed:{user_guess}')
list1=['0','','']
shuffled_list=generate_random(list1)
print(f'Shuffled list is :{shuffled_list}')
check_match(shuffled_list,user_guess)


