def compressString(string) :
    count = 0
    res, temp = '', ''
    for i in string :
        if i!=temp :
            res += temp

            if count>1 :
                res += str(count)
            
            temp = i
            count = 1
        else :
            count +=1
    else :
        res += temp
        if count>1 :
            res += str(count)

    return res

string = input()
string = compressString(string)
print(string)