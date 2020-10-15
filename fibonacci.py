def fib(n):
    x = 0
    y = 1
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        print(x)
        print(y)
        for i in range(2, n):
            
            z = x + y
            x = y
            y = z
            
            
            
            
            print(z)
fib(2)                 