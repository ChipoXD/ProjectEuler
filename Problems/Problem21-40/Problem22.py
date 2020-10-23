# ProblemURL: https://projecteuler.net/problem=22
f = open('Problem22data.txt', 'r')
content = f.read().split("\",\"")
f.close()
content[0] = content[0][1:]
content[-1] = content[-1][:-1]
content.sort()

totalSum = 0
for name in content:
    nameSum = 0
    for c in name:
        nameSum += (ord(c) - 64)
    nameSum *= (content.index(name) + 1)
    totalSum += nameSum

print(totalSum)
