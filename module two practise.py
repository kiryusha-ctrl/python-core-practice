def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Старт")
        func(*args, **kwargs)
        print("Финиш")
    return wrapper

@my_decorator
def greet(name):
    print(f"Привет, {name}!")

greet("Кирюха")