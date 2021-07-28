def existing_func():
    print("Am the existing function")

def new_decorator(new_func):
    def wrap_func():
        print("Code added before decorator")

        new_func()

        print("Code added after decorator")
    return wrap_func()



decorator_func=new_decorator(existing_func)
decorator_func
print('******************************************************')
#instead of creating frame work this way , we can add decorator to the existing function
@new_decorator
def existing_func():
    print("Am the existing function")

