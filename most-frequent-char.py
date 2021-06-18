from typing import Counter


def mostFrequentChar(string) :
    counter,count = 0,0
    ch,temp = '',''

    string = ''.join(sorted(string))
    for i in string :
        if i!=temp :
            if count>counter :
                counter = count
                ch = temp
            
            count = 1
            temp = i
        else :
            count += 1
    
    if count>counter :
        ch = temp

    return ch

string = input()
print(mostFrequentChar(string))