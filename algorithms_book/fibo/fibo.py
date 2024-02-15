def fibo(n):
    fib1 = fib2 = 1
    res = [0]
    for i in range(n):
        res.append(fib1)
        fib1, fib2 = fib2, fib2 + fib1
    return res


print(fibo(10))
