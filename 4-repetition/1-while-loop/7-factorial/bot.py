print("Please enter a number?")
num = int(input())
factorial = 1
while num > 0:
        factorial = factorial * num
        num -=1
print("The factorial is " + str(factorial))
