loop = 5
health = 100
print("Your health is" + str(health) + "%. Escape is in progress...")
while loop >= 5:
    print("...Oh dear, who is that?")
    user = input()
    if user == "Smiler's Bot":
        print("Time to jam out of here.")
        health -= 20
    elif user == "Hacker":
        print("Yay! Better follow this one!")
        health += 20
    else:
        print("Phew! Just another emoji.")

else:
    print("Escaped! Health is " + str(health) + "%.")