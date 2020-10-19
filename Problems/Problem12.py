# ProblemURL: https://projecteuler.net/problem=12
def primefactors(x):
    primes = []
    numbers = [x]
    while numbers:
        found = False
        temp = []
        for number in numbers:
            for i in range(2, int(number), 1):
                if number % i == 0:
                    temp.append(i)
                    temp.append(number / i)
                    found = True
                    break
            if not found:
                primes.append(int(number))
        numbers = temp
    return primes


def trianglenumber(x):
    return x*(x+1)/2


def fact(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


def propperdivisors(mylist):
    d = 1
    uniqueList = list(set(myList))
    for unique in uniqueList:
        d *= (myList.count(unique) + 1)
    return d


n = 0
propperDivisors = 0
while propperDivisors < 500:
    n += 1
    tri = trianglenumber(n)
    myList = primefactors(tri)
    propperDivisors = propperdivisors(myList)
    print(f"{int(tri)}: {propperDivisors} - {myList}")
