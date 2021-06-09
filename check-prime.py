n = int(input())
i = int(2)
ch = False

while i<n :
    if n%i == 0 :
        ch = True
    i += 1

if ch :
    print("Not Prime")
else :
    print("Prime")