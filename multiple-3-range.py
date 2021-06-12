# multiples of 3 in [a,b]
a = int(input('Enter value of a : '))
b = int(input('Enter value of b : '))

if a%3==0 :
    s = a
elif a%3==1 :
    s = a+2
else :
    s = a+1

for i in range(s,b+1,3) :
    if i%3 == 0 :
        print(i)