n = int(input())
sumE = 0
sumO = 0

while n>0 :
    a = n%10
    
    if a&1 :
        sumO = sumO+a
    else :
        sumE = sumE+a
        
    n = n//10
    
print(sumE, sumO , sep=" ")