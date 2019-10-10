print("How many rows should I have?")
row = int(input())
print()
print("How many columns should I have?")
col = int(input())
print()
print("Here I go:")
for count in range(0, row, 1):
    for number in range(0, col, 1):
        print(":-) ", end="")
    print()
print("\nDone!")