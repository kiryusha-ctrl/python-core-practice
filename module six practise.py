import time
import threading

def heavy_computation():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

def measure_time(func, use_thread=False):
    start_time = time.time()  # Засекаем время ДО
    
    if use_thread:
        # 1. Создаём поток. target=функция (без скобок!), args=кортеж аргументов (если есть)
        thread = threading.Thread(target=func)
        # 2. Запускаем поток
        thread.start()
        # 3. Ждём, пока поток закончит работу
        thread.join()
    else:
        # Обычный вызов функции
        func()
        
    end_time = time.time()    # Засекаем время ПОСЛЕ
    print(f"Время выполнения: {end_time - start_time:.4f} сек.")

print("1. Обычный вызов:")
measure_time(heavy_computation, use_thread=False)

print("\n2. Вызов в потоке:")
measure_time(heavy_computation, use_thread=True)