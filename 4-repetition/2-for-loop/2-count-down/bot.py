print("How far are we from the cave?")
num = int(input())
print()
while num >= 1:
    print(str(num) + " steps remaining")
    num -= 1
else:
    print()
    print("We have reached the cave!")
