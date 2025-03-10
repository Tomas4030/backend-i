import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Call to {func.__name__} with args: {args}, result: {result}")
        print(f"Execution time: {time.time() - start_time:.4f} seconds")
        return result
    return wrapper

users = ["tomas", "miguel"]

def authenticate(func):
    def wrapper(username, *args, **kwargs):
        if username not in users:
            print("Authentication failed!")
            return None
        return func(username, *args, **kwargs)
    return wrapper

@log_calls
@authenticate
def access_system(username):
    return f"Login {username}"

print(access_system("tomas")) 
print("------------------------")
print(access_system("lucas"))  
