print("How many numbers should I sum up?")
num = input()
boop = 1
total = 0
imp = 0
print()
while boop <= int(num):
    print("Please enter number " + str(boop) + " of " + str(num))
    boop += 1
    value = int(input())
    total = value + total
else:
    print()
    print("The answer is " + str(total), ".")