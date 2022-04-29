userinp = input('enter a string ')

numberOfTimes = int(len(userinp)/4)

b_num = list(userinp)

myarr = []

for i in range(numberOfTimes):
    value = 0
    for i in range(4):
        digit = b_num.pop()
        if digit == '1':
            value = value + pow(2, i)
        
    myarr.append(value)
        
myarr.reverse()
print(''.join(map(str,myarr)))
