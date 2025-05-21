# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().



def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello Maha!")

say_hello()


# PS: If we want to create a decorator that works with functions
# having any number of positional or keyword arguments, then we
# can use *args and **kwargs in the wrapper function.
