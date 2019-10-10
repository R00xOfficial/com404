print("How many mountains should I display?")
num = int(input())

print("Displaying...")
print()
while num >= 1:
    print("           __")
    print("          /  \\_")
    print("         /^    \\ ")
    print("        /  ^    \\_")
    print("      _/ ^ ^     ^\\ ")
    print("     /  ^     ^    \\ ")
    num -= 1
else:
    print()
    print()
    print("Done!")