"""The code contains the list from the spam.py but the challenge here is that, we have to print the menues with the word 
"spam" removed from each one where required."""

menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs", "bacon", "sausage","spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "eggs","spam","spam","bacon","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
]


for item in menu:
    for idx, each in enumerate(item):
        if each == "spam":
            del item[idx]
    
    print(item)

