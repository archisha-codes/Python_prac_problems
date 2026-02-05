def fibo(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        it = fibo(10)
        print (it)