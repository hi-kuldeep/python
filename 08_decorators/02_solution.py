

def debug(func):
    def wrapper(*args , **kwargs):
        func_name = func.__name__
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join( f"{k}:{v}" for k, v in kwargs)
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
def greeting(name , message):
    print(f"{message} , {name}")

hello()
greeting("kuldeep" , "Good Morning")
