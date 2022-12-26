menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs", "bacon", "sausage","spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "eggs","spam","spam","bacon","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
]

for meal in menu:
    for index in range(len(meal)-1, -1, -1):
        if meal[index]== "spam":
            del meal[index]
    print(", ".join(meal))