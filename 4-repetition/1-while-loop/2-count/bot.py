print("How many live cables should I avoid?")
num = input()


while num > 0:
    print("Avoiding...Done! " + num + "live cables avoided.")
    num -=  1
else:
    print("All live cables have been avoided.")