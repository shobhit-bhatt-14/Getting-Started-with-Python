def removeChar(string, x) :
    string = string.replace(x,'')
    return string

string = input()
x = input()
print(removeChar(string,x))