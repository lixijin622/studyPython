def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        # print(b)
        a, b = b, a+b  # !!!
    print()
    return 'haha'

fib(20)
f = fib
f(10)
print(fib(10))
