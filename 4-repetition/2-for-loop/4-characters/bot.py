print("What strange markings do you see?")
user_word = input()
print("Identifying...")
print()
num = 0
for position in range(0, len(user_word), 1):
    print("index " + str(num) + ": " + (user_word[position]))
    num += 1
else:
    print()
    print("Done!")
