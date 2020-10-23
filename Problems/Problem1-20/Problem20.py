# ProblemURL: https://projecteuler.net/problem=20
def fact(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


a = fact(100)
myList = [int(x) for x in str(a)]
print(sum(myList))