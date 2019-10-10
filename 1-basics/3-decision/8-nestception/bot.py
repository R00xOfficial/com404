print("Where should I look?")
which_room = input()

if (which_room == "in the bedroom"):
    print("where in the bedroom should i look?")
    which_place_bedroom = input()
    if (which_place_bedroom == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

elif (which_room == "in the bathroom"):
    print("Where in the bathroom should I look?")
    which_place_bathroom = input()
    if(which_place_bathroom == "in the bathtub"):
        print("found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")

elif (which_room == "in the lab"):
    print("Where in the lab should I look?")
    which_place_lab = input
    if (which_place_lab == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
else:
    print("I do not know where that is but I will keep looking.")