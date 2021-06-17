def countType(str):
    vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    countN,countV,countC,countS = 0,0,0,0

    for i in str:
        if i>='0' and i<='9':
            countN += 1
        elif i in vow:
            countV += 1
        elif (i>='A' and i<='Z') or (i>='a' and i<='z'):
            countC += 1
        else :
            countS += 1

    print("Numbers = {}\nVowels = {}\nConsonants = {}\nSpecial Characters = {}".format(countN,countV,countC,countS))

str = input()
countType(str)