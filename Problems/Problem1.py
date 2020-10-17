# ProblemURL: https://projecteuler.net/problem=1
a = 3
b = 5
c = 1000
sumOfMultiples = 0
for i in range(c):
    if i % 3 == 0 or i % 5 == 0:
        sumOfMultiples += i
print(sumOfMultiples)