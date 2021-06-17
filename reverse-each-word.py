def reverseEachWord(string) :
    res = ""
    li = list(string.split())
    for s in li :
        res += s[::-1]
        res += ' '
    
    return res

string = input()
string = reverseEachWord(string)
print(string)