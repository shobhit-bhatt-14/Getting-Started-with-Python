def checkPalindrome(num):
    n = num
    rev = 0
    while num>0:
        a = num%10
        rev = (rev*10)+a
        num = num//10
    
    if rev==n:
        return True
    else:
    	return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')