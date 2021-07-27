#if the script is run directly as One.py then __name__ =__main__
def func():
    print("func in one.py")

print("Top level in One.py")

if __name__=="__main__":
    print("One.py is being run directly")
else:
    print("One.py is being imported")
