# Permutation means getting same strings on rearranging the characters

def isPermutation(string1, string2) :
    n,m = len(string1),len(string2)
    
    if n!=m or n==0 or m==0 :
        return False
    else :
        string1 = ''.join(sorted(string1))
        string2 = ''.join(sorted(string2))
        if string1!=string2 :
            return False

    return True

string1 = input()
string2 = input()
print(isPermutation(string1,string2))