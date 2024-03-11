number=[10,20,30,40]
number.insert(1,15)
number2=[50,60,70]
number.extend(number2)
del number[-1]
number.sort()
print(number)