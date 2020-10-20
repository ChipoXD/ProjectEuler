# ProblemURL: https://projecteuler.net/problem=21
import itertools


def primefactors(x):
    primes = []
    numbers = [x]
    if x < 2:
        return []
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


def devisorfromprimefactor(mylist):
    tempList = []
    unqieList = list(set(mylist))
    for unqiue in unqieList:
        a = []
        for n in range(1, mylist.count(unqiue) + 1, 1):
            a.append(unqiue**n)
        tempList.append(a)
    return tempList


def allproductpairs(mylist):
    output = []
    for x in mylist:
        x.append(1)
    combination = list(itertools.product(*mylist))
    for x in combination:
        temp = 1
        for y in x:
            temp *= y
        output.append(temp)
    output.sort()
    output.pop(-1)
    return output


amicableNumber = []
for i in range(220, 10001):
    xprimefactors = primefactors(i)
    xdevisors = devisorfromprimefactor(xprimefactors)
    xproductpairs = allproductpairs(xdevisors)
    xsum = sum(xproductpairs)

    yprimefactors = primefactors(xsum)
    ydevisors = devisorfromprimefactor(yprimefactors)
    yproductpairs = allproductpairs(ydevisors)
    ysum = sum(yproductpairs)

    if ysum == i and i != xsum:
        amicableNumber.append(i)
print(amicableNumber)
print(sum(amicableNumber))
