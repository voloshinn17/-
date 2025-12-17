import time

def timing(f, n, a):
    print(f.__name__)
    r = range(n)
    t1 = time.perf_counter()
    for i in r:
        f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a)
    t2 = time.perf_counter()
    print(round(t2-t1, 3))