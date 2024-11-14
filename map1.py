def square(n):
    return n*n

numbers = [8,10,20,40,60]
squares = map(square,numbers)

print(list(squares))

number1 = [5,6,7,8,9]
number2 = [10,11,12,13,14]

result = map(lambda x,y:x+y, number1, number2)
print(list(result))