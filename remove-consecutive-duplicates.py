def removeConsecutiveDuplicates(string) :
    res = ''
    temp = ''
    for ch in string :
        if ch != temp :
            temp = ch
            res += temp
    
    return res

string = input()
string = removeConsecutiveDuplicates(string)
print(string)