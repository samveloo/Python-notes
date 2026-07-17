fib = [1, 1]
n = int(input())

if n == 1:
    print(1)
else:
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    print(*fib)