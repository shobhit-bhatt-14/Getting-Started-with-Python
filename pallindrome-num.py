def checkPalindrome(num):
    n = str(num)
    rev = ''
    while num>0 :
        a = num%10
        rev = rev+str(a)
        num = num//10
        
    if n == rev :
    	return True
    else :
        return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')