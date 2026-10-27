import time

def dec_timer(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f"функция заняла {finish - start} секунд")
        return result
    return timer
@dec_timer
def slow_function():
    for i in range(1000000):
        pass
    return "Готово!"

print(slow_function())