myList = []
for a in range(2, 101, 1):
    for b in range(2, 101, 1):
        myList.append(a**b)
myList2 = list(set(myList))
print(len(myList2))