# structure of a Python dictionary
dic = {1:'a' , 2:2 , 'c':3}
print(dic)
print(type(dic))

# copy dictionary
b = dic.copy()
print(b)

# making a new dictionary
d = dict({("the",1) , ("hello",2) , ("world",3)})
print(d)

# dictionary with keys => value is none
dc = dict.fromkeys({"abc" , 1 , 5 , 'a'})
print(dc)

# dictionary with keys and same value
s = dict.fromkeys({'a' , 'b' , 'c' , 1 , 2 , 3 , 4} , "hello")
print(s)