mylist = [1]
n = 1
while n < 1001:
    n += 2
    mylist.append((n - 1) + mylist[-1])
    mylist.append((n - 1) + mylist[-1])
    mylist.append((n - 1) + mylist[-1])
    mylist.append((n - 1) + mylist[-1])
print(sum(mylist))