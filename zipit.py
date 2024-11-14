number1 = [1,2,3,4,5]
number2 = ["a", "b", "c", "d", "e"]

number3 = zip(number1, number2)
print(list(number3))

number4 = [1,2,3,4,5]
number5 = [1,2,3,4,5]

for x,y in zip(number4, number5[::-1]):
    print(x,y)