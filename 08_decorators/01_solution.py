import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start}")
        return result
    return wrapper

@timer
def example_fn(n):
    time.sleep(n)
    return n

example_fn(2)