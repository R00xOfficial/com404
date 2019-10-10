print("what type of cover does the book have?")
cover = input()

if (cover == "soft"):
    print("is the book perfect bound?")
    bound = input()
    if (bound == "yes"):
        print("soft cover, perfect bound books are very popular!")
    elif (bound == "no"):
        print("Soft covers with coils or stitches are great for short books")
elif (cover == "hard"):
    print("Books with hard covers can be more expensive!")