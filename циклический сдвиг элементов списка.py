def cyclic_shift(numbers: list[int | float], step: int) -> None:
    a = [numbers[(i - step) % len(numbers)] for i in range(len(numbers))]
    numbers.clear()
    for i in a:
        numbers.append(i)


# этот видимо оптимальный 
# есть статья https://sky.pro/wiki/python/optimalnoe-vraschenie-spiska-v-python-effektivnost-i-kod/
def c_yclic_shift(numbers: list[int | float], step: int) -> None:
    step %= len(numbers)
    numbers[:] = numbers[-step:] + numbers[:-step]