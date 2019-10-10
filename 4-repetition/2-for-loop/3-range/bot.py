print("What level of brightness is required?")
num = int(input())
points = 2
print("Adjusting brightness...")
for count in range (2, num + 1, 2):
    print()
    print("Beep's brightness level:" + "*" * points)
    print("Bop's brightness level:" + "*" * points)
    print()
    points += 2
else:
    print("Adjustments complete!")