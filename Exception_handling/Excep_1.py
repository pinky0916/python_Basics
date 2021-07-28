def int_check():
    while True:

      try:
          num=int(input("Enter a number:"))
      except:  # This will get executed if there is an error
          print("OOps,that is not a number Enter the integer")
          continue
      else:  # only if there are no errors in try block
          print("Congrats,You entered an integer")
          break
      finally: # will get executed if there are errors or not
          print("Executing finally")
          print("You are at the end of the code")

int_check()
print ('******************************************************')

# to show the in built error along with user error message
a=5
b=0
try:
    print(a/b)
except Exception as a: # object of the Exception
    print("Division by zero is not possible:",a)
print("Done")

print ('******************************************************')


