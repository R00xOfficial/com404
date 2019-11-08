print("How many miles must I travel before I reach the secret base?")
var = int(input())
print("I will count the miles...")
print()
while var > 0:
    print("I have " + str(var) + " miles to go before I reach the base.")
    var -=  1
else:
    print()
    print("I have arrived at the secret headquarters of the MIB!")
    print("It is time to sneak in.")