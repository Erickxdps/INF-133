from funcstools from wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la funcion")
        result = func(*args, **kwargs)
        print("Despues de llamar a la funcion")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Funcion para saludar a alguien"""
    print(f"Hola, {name}!")
    
    
greet("Juan")
print(greet.__name__)
print(greet.__doc__)