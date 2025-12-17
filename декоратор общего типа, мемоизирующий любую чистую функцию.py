import functools

def cached(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        result = cache.get(key)
        if result is None:
            result = func(*args, **kwargs)
            cache[key] = result
        return result
    return wrapper

#key = args + tuple(kwargs.items())
#тоесть ключ индивидуален и больше по комбинации этих аргументов никакого другого результата не получится?
#ключ действительно уникально характеризует каждую комбинацию аргументов, и ни при каком другом сочетании 
# аргументов такого же результата получено быть не может.