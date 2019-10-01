print("How many days remain until the next full moon?")
number = int(input())
print("We must count the days...")
print()
while number > 0:
    print("The full moon will be upon us in " + str(number) + " days.")
    number -=  1
else:
    print()
    print("It's a full moon. The beast has been unleashed!")
    print("May it have mercy on our souls.")