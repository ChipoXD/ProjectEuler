import itertools

def allsumpairs(mylist):
    output = []
    combination = list(itertools.product(*mylist))
    for x in combination:
        temp = 0
        for y in x:
            temp += y
        if temp not in output:
            output.append(temp)
    output.sort()
    return output

mylist1 = [[1, 2], [3, 4]]
mylist2 = [[2, 4, 1], [3, 1], [103, 1]]

combination = allsumpairs(mylist1)
print(combination)