#for each operation a new address is used
a = 10
print('Address a : ' + str(id(a)))
a = a+1
print('Address a+1 : ' + str(id(a)))

#in range [-5,256] the variable with same value point to a common address
x = 10
y = 10
print('Address x : ' + str(id(x)))
print('Address y : ' + str(id(y)))