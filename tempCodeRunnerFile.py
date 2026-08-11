num = 586
while num > 0:
    last_digit = num % 10
    print(last_digit, sep='*', end='#')
    num //= 10
    print()