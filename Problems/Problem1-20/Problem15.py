# ProblemURL: https://projecteuler.net/problem=15
def fact(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


def binomial(argin1, argin2):
    return (fact(argin1))/(fact(argin2)*(fact(argin1-argin2)))


a = 20
print(binomial(a*2, a))
