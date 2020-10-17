# ProblemURL: https://projecteuler.net/problem=3
numbers = [600851475143]
primes = []
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
primes.sort()
print(primes)
print(primes[-1])
