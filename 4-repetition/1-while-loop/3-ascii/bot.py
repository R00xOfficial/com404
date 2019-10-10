print("How many bars should be charged?")
num = int(input())
bars = 1
print()
while num > 0:
    print("Charging: " + ('█' * int(bars)))
    num -= 1
    bars += 1
else:
    print()
    print("The battery is fully charged.")