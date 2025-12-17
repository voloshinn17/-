def f1(left, right):
    while left <= right:
        flag = True
        for i in range(2, left // 2 + 1):
            if left % i == 0:
                flag = False
        if flag and left != 1:
            yield left
        left += 1
        flag = True
generator = f1(1, 15)



# Решето_Эратосфена
from typing import Generator


def f(left: int, right: int) -> Generator:
    sieve = [False] * 2 + [True] * (right - 1)
    for i in range(2, right):
        if sieve[i]:
            for j in range(i * 2, right + 1, i):
                sieve[j] = False
    return (digit for digit, value in enumerate(sieve) if value and digit >= left)


#еще с использованием функций 
from math import sqrt

def primes(left, right):
    left = max(2, left)
    for num in range(left, right + 1):
        if all(map(lambda x: num % x != 0, range(2, int(sqrt(num)) + 1))):
            yield num

# если сумма всех делителей числа равна (само число + 1)
def is_prime(number: int):
    return sum(x if number % x == 0 else 0 for x in range(1, number + 1)) == number + 1            