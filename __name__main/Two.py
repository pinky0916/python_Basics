from __name__main import One
One.func()

print("Top level of two.py")
if __name__=="__main__":
    print("two.py is executed directly")
else:
    print("Two.py is imported")
