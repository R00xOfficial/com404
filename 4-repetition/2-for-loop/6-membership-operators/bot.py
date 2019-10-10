print("What phrase do you see?")
s = input()
print()
print("Reversing...")
chars = list(s)
for i in range(len(s) // 2):
    tmp = chars[i]
    chars[i] = chars[len(s) - i - 1]
    chars[len(s) - i - 1] = tmp
print()
print( ''.join(chars))