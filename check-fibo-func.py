def checkMember(n):
    a = 0
    b = 1
    if n==a or n==b:
        return True
    
    c = a+b
    while c<=n :
        if c==n:
            return True
        a = b
        b = c
        c = a+b
        
    return False
        
    
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")