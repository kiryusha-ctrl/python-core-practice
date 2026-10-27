listik = []
for i in range(100000):
    listik.append(i)

def chetnik(lst):
    for i in lst:
        if i % 2 == 0:
            yield i

# Шаг 1: Создаем генератор
gen = chetnik(listik)

# Шаг 2: Проходимся циклом
for i in gen:
    print(i)
    if i > 10:  # Остановимся после 10, чтобы не печатать 50000 чисел
        break

# Шаг 3: Доказываем одноразовость
print("\nПопытка пройти второй раз:")
for i in gen:
    print(i)  # ← Это ничего не выведет!