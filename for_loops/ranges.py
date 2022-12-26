my_list = [15,23,56,89,2,0,59,78,235,65,89]

for enu, i in enumerate(my_list):
    if i == 0:
        my_list[enu] = int((my_list[enu-1]+my_list[enu+1])/2)

print(my_list)
