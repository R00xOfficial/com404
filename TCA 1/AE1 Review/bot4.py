var = "I wonder what is in my suitcase..."

def item_from_suitcase(item):
    if item == "toothbrush":
        print(var)
        print("A toothbrush! Well, got to have clean teeth.")
        print()
    elif item == "belt":
        print(var)
        print("An unexpected item! It could be useful.")
        print()
    else:
        print(var)
        print("My Spidey suit! I won't be needing this. I am on holiday.")
        print()

item_from_suitcase("toothbrush")
item_from_suitcase("belt")
item_from_suitcase("spidey suit")