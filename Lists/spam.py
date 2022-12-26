menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs", "bacon", "sausage","spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "eggs","spam","spam","bacon","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
]

 # select the nested list which does not contain "spam" in it
for item in menu:
    if "spam" not in item:
        print(item)

        for content in item:
            print(content)

    # We can use the count() method in the sequence type to check how many times the word "spam" appers in the list
    else:
        print("{0} has a spam count of {1}"
        .format(item, item.count("spam")))