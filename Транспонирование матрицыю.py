n = 10
matrix = [[1] * n for _ in range(n)] 
matrix = list(map(lambda x: list(x), zip(*matrix)))

for row in matrix:
    print(*row)
