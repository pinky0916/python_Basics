def user_choice():
    user_index=''
    while user_index not in ['0','1','2']:
        user_index=input("Enter an index position 0,1 or 2:")
    return int(user_index)

def random_num_gen(my_list1):
    shuffle(my_list1)
    return my_list1

def guess_check(rand_list,user_index1):
    for x,y in enumerate(rand_list):
      print(x,y)
      if y !='':
          print('Ho')
          if x==user_index1:
              print("Wow ,user has guessed right")
              break;
          else:
              print("Oops guessed wrongly")
              break;
      else:
          pass

def guess_check1(rand_list,user_index1):
    elem=next(a for a in rand_list if a)
    elem_index=rand_list.index(elem)
    print(f'Guess check1:{elem} is at index position {elem_index}')
    if elem_index==user_index1:
        print("WOW,you guessed it right")
    else:
        print('OOps,you guessed it wrong)')

def guess_check2(rand_list,user_index1):
    if rand_list[user_index1]=='O':
        print("WOW,you guessed it right")
    else:
        print('OOps,you guessed it wrong)')





from random import shuffle
user_index1=user_choice()
print(f'User guess is {user_index1}')
my_list=['','O','']
rand_list=random_num_gen(my_list)
print(f'Random list generated is:{rand_list}')
guess_check2(rand_list,user_index1)