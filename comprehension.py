# list1 = []
# for i in range(5):
#     for j in range(3, 20):
#         list1.append(j)

# print(list1)

# list2 = [j for i in range(5) for j in range(3, 6)]

# list3 = [j for j in list1 ]
# print(list2)
# print(list3)


list1 = [i for i in range(20)]
print(list1)
list2 = [i for i in range(20, 40)]

print(list2)

dict = {var:key for var, key in zip(list1, list2)}
print(dict)