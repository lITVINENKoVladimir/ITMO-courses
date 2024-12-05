import functools
import datetime
import os

call_stats = {} # Храним статистику вызовов здесь

def count_calls(func):
    """Декоратор для подсчета вызовов функции."""
    func_name = func.__name__
    call_stats[func_name] = {'call_count': 0, 'last_call_time': None}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        call_stats[func_name]['call_count'] += 1
        call_stats[func_name]['last_call_time'] = datetime.datetime.now()
        return func(*args, **kwargs)

    return wrapper

def save_stats(filename="debug.log"):
    """Сохраняет статистику вызовов функций в файл."""
    with open(filename, "w") as f:
        for func_name, data in call_stats.items():
            f.write(f"{func_name},{data['call_count']},{data['last_call_time'].strftime('%d.%m.%Y %H:%M') 
             if data['last_call_time'] 
             else 'Never called'}")
    print(f"Статистика сохранена в файл {filename}")


@count_calls
def render(a, b, c):
    return a + b + c

@count_calls
def show(text):
    print(text)
    return text

@count_calls
def process_data(data):
    time.sleep(0.1)  # Симуляция работы
    return len(data)

import time

# Вызовы функций (необходимо вызывать функции!)
render(1, 2, 3)
show("Hello, world!")
render(4, 5, 6)
process_data([1, 2, 3, 4, 5])
show("Another message")
render(10, 20, 30)
process_data([1, 2, 3, 4, 5, 6, 7, 8])


save_stats()