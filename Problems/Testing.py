import itertools


mylist1 = [[1, 2], [3, 4]]
mylist2 = [[2, 4, 1], [3, 1], [103, 1]]

combination = list(itertools.product(*mylist2))
print(combination)