fib = [1, 1]
n = int(input())

for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])

print(*fib)