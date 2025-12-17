#Иногда полезно иметь декоратор, который может отслеживать состояние вызова функции. 
# Создадим декоратор, который подсчитывает, сколько раз вызывается функция. 
# Для сохранения состояния счетчика будем использовать пользовательский атрибут функции.
# ДЕКОРАТОР РАБОЧИЙ VS Code просто предостерегает убери лишние # в коде

import functools
from typing import Any
def counter(func):
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        #wrapper.num += 1
        #print(f'Вызов {func.__name__}: {wrapper.num}')
        val = func(*args, **kwargs)
        return val
    # wrapper.num = 0
    return wrapper

@counter
def greet(name: str) -> str:
    return f'Hello {name}!'

print(greet('Timur'))
print(greet('Ruslan'))
print(greet('Arthur'))
print(greet('Gvido'))