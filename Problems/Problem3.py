# ProblemURL: https://projecteuler.net/problem=3
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


output = primefactors(600851475143)
print(output)
print(output[-1])
