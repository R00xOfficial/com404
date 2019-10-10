print("Please enter the first whole number.")
num1 = int(input())
print("Please enter the second whole number.")
num2 = int(input())
print("Please enter the third whole number.")
num3 = int(input())
print()
odd = 0
even = 0
if (num1%2==0):
    even = even + 1
else:
    odd = odd + 1

if (num2%2==0):
    even = even + 1
else:
    odd = odd + 1

if (num3%2==0):
    even = even + 1
else:
    odd = odd + 1

print("There were " + str(even) + " even and " + str(odd) + " odd numbers.")
