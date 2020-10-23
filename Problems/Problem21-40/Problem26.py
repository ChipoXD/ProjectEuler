# ProblemURL: https://projecteuler.net/problem=26
from decimal import getcontext, Decimal
getcontext().prec = 100


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


def isfracrepeatingfromprimefactor(argin):
    if len(argin) == 1 and argin[0] == 1:
        return False
    if argin.count(2) + argin.count(5) == len(argin):
        return False
    return True


biggestk = 0
biggestkIndex = 0
for i in range(1, 10001):
    print(f"{i}: {primefactors(i)}, reapeatable: {isfracrepeatingfromprimefactor(primefactors(i))}")
    if len(primefactors(i)) == 1 and isfracrepeatingfromprimefactor(primefactors(i)):
        k = 1
        while ((10**k)-1) % i != 0:
            k += 1
        if k > biggestk:
            biggestk = k
            biggestkIndex = i
        print(f"Repeating digits: {k}")
print(f"Largest repeating size: {biggestk} at index: {biggestkIndex}")