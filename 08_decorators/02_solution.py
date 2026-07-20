

def debug(func):
    def wrapper(*args , **kwargs):
        func_name = func.__name__
        # handling position arguments
        args_value = ', '.join(str(arg) for arg in args)
        # handling keyword arguments
        kwargs_value = ', '.join( f"{k}:{v}" for k, v in kwargs.items())
        # check if no argument are passed
        no_args = len(args) == 0 and len(kwargs) == 0
        if not no_args:
            print(f"Calling {func_name}({args_value} , {kwargs_value})")
        else:
            print(f"Calling {func_name}(without arguments)")
        return func(*args, **kwargs)
    return wrapper


@debug
def hello():
    print("Hello World!")
    
@debug
def greeting(name , message="Namaste"):
    print(f" {name}")

hello()
greeting("kuldeep" , message="Good Morning")
