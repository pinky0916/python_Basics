

try:

    k = int(input('Enter a number'))
except ZeroDivisionError as a: # object of the Exception
    print("Division by zero is not possible:",a)
except ValueError:
    print("value Error:Enter an integer:")
except Exception as e:
    print("General error")
print("Done")