# ProblemURL: https://projecteuler.net/problem=27
def primefactors(x):
    if x < 0:
        return []
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


def quadraticsprimeform(argin1, argin2):
    n = 0
    while len(primefactors(n**2 + argin1*n + argin2)) == 1:
        n += 1
    return n


def quadraticsprimeformprint(argin1, argin2):
    n = 0
    while len(primefactors(n**2 + argin1*n + argin2)) == 1:
        n += 1
        print(n**2 + argin1*n + argin2)
    return n


besta = 0
bestb = 0
bestn = 0
print(quadraticsprimeform(-79, 1601))
print(quadraticsprimeform(1, 41))
print(primefactors(-1000))

usefulb = []
for b in range(2, 1001, 1):
    if len(primefactors(b)) == 1:
        usefulb.append(b)

for b in usefulb:
    print(b)
    for a in range(-999, 1000, 1):
        if bestn < quadraticsprimeform(a, b):
            bestn = quadraticsprimeform(a, b)
            besta = a
            bestb = b
            print(f"a:{besta}, b:{bestb}, n:{bestn}")
print(f"a:{besta}, b:{bestb}, n:{bestn}")