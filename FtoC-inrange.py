# F to C from s to e with step of w
s = int(input("Starting Point : "))
e = int(input("Ending Point : "))
w = int(input("Dip : "))

while s<=e :
    cel = (s-32)*5/9
    cel = int(cel)
    print(str(s)+"\t"+str(cel))
    s += w