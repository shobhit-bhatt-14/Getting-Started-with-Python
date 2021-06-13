def checkArmstrong(num):
    n = num
    arm = 0
    len = 0
    
    while num>0:
        len = len+1
        num = num//10
    num = n
    
    while num>0:
        a = num%10
        arm = arm + (a**len)
        num = num//10
        
    if arm==n:
        return True
    else:
    	return False
		
num = int(input())
isArmstrong = checkArmstrong(num)
if(isArmstrong):
	print('true')
else:
	print('false')