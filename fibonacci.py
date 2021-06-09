def fibo(a, b, c) :
    if c==0 :
        return b
    
    b = a+b
    a = b-a
    c = c-1
    
    return fibo(a, b, c)

n = int(input())
a = 1
b = 1
if n==1 or n==2 :
    print(1)
else :
    print(fibo(a, b, n-2))